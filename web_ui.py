"""
Web UI Server for Zara AI - Orb Interface
Handles WebSocket communication between the orb UI and the AI backend
"""

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import threading
import queue
import time
from voice.speaker import speak
from voice.listener import listen
from ai.gemini_ai import get_response
from tasks.general_tasks import execute_command
import os
from datetime import datetime

# Import translation functions
from translator.speech_input import recognize_speech
from translator.translator_engine import translate_tamil_to_hindi
from translator.speech_output import speak_text

# Import Spotify functions
import webbrowser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zara-orb-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Queue for communication between threads
command_queue = queue.Queue()
response_queue = queue.Queue()

# Logging function
def log_conversation(role, message):
    log_path = os.path.join(os.getcwd(), "conversation_log.txt")
    with open(log_path, "a", encoding="utf-8") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {role}: {message}\n")

# State management
current_state = {"status": "ready"}

def update_orb_state(state):
    """Update the orb state and emit to all connected clients"""
    current_state["status"] = state
    socketio.emit('state_change', {'state': state})
    print(f"🔄 Orb state changed to: {state}")

def search_and_play_song_no_auth(song_query):
    """Search and play song on Spotify (web version)"""
    try:
        search_url = f"https://open.spotify.com/search/{song_query.replace(' ', '%20')}"
        webbrowser.open(search_url)
        
        success_msg = f"{song_query} Spotify இல் தேடப்பட்டது!"
        print(f"🌐 {success_msg}")
        speak(f"{song_query} Spotify இல் தேடுகிறேன்.")
        log_conversation("Assistant", f"Searched Spotify for: {song_query}")
        return True
    except Exception as e:
        error_msg = f"பிழை: {e}"
        print(f"❌ {error_msg}")
        speak("Spotify தேடலில் பிழை.")
        return False

def process_command(command):
    """Process user commands"""
    if not command:
        return

    print(f"[USER COMMAND]: {command}")
    log_conversation("User", command)

    # Update orb to processing state
    update_orb_state('processing')

    # Check for specific commands
    
    # Spotify/music command
    if any(kw in command.lower() for kw in ["play song", "play music", "spotify", "பாடல் இசை", "இசை இசை", "song play", "music play"]):
        update_orb_state('speaking')
        song_msg = "எந்த பாடலை கேட்க விரும்புகிறீர்கள்? பாடல் பெயரை சொல்லுங்கள்."

        # Send to browser for speech synthesis
        socketio.emit('speak_text', {'text': song_msg})

        try:
            speak(song_msg)
        except Exception as e:
            print(f"⚠️ Local audio playback failed: {e}")

        update_orb_state('ready')
        # Browser will listen and send the song name as next command
        return

    # If direct song search (contains "play" + song name)
    if "play" in command.lower() and len(command.split()) > 1:
        parts = command.lower().split("play", 1)
        if len(parts) > 1:
            song_name = parts[1].strip()
            if song_name:
                update_orb_state('speaking')
                search_and_play_song_no_auth(song_name)
                update_orb_state('ready')
                return

    # If general task command
    if execute_command(command):
        log_conversation("Assistant", "Executed general task command.")
        update_orb_state('ready')
        return

    # Use Gemini AI to respond
    response = get_response(command)
    log_conversation("Assistant", response)
    update_orb_state('speaking')

    # Check if response is from fallback (contains certain keywords)
    is_fallback = any(phrase in response for phrase in [
        "மன்னிக்கவும், நான் தற்போது",
        "விரிவான பதில்கள் கொடுக்க முடியாது"
    ])

    # Send text to browser for speech synthesis with fallback indicator
    socketio.emit('speak_text', {
        'text': response,
        'is_fallback': is_fallback
    })

    # Try to speak locally (will fail in container, but that's ok)
    try:
        speak(response)
    except Exception as e:
        print(f"⚠️ Local audio playback failed (expected in container): {e}")

    update_orb_state('ready')

def ai_interaction_loop():
    """Main AI interaction loop - just sends welcome and waits for browser commands"""
    print("🤖 AI Interaction Loop Started")
    print("📱 Voice recognition will happen in the browser (on your phone)")
    
    # Welcome message
    welcome_msg = "வணக்கம்! நான் ஜாரா. இன்று நான் உங்களுக்கு எப்படி உதவ முடியும்?"
    update_orb_state('speaking')
    time.sleep(0.5)  # Give time for state to propagate

    # Send welcome message to browser for speech synthesis
    socketio.emit('speak_text', {'text': welcome_msg})

    # Try to speak locally (will fail in container, but that's ok)
    try:
        speak(welcome_msg)
    except Exception as e:
        print(f"⚠️ Local audio playback failed (expected in container): {e}")

    log_conversation("Assistant", welcome_msg)
    update_orb_state('ready')
    
    print("✅ AI ready - waiting for voice commands from browser...")
    
    # Keep thread alive
    while True:
        time.sleep(10)
        # Just keep alive, all interaction happens via WebSocket events

@app.route('/')
def index():
    """Serve the main orb UI page"""
    return render_template('orb_ui.html')

@app.route('/status')
def status():
    """Get current status"""
    return jsonify(current_state)

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    print('🔌 Client connected')
    
    # Send current state
    emit('state_change', {'state': current_state["status"]})
    
    # Send welcome message to newly connected client
    time.sleep(0.5)  # Small delay to ensure client is ready
    welcome_msg = "வணக்கம்! நான் ஜாரா. இன்று நான் உங்களுக்கு எப்படி உதவ முடியும்?"
    emit('speak_text', {'text': welcome_msg})
    print(f"📢 Sent welcome message to client")

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    print('🔌 Client disconnected')

@socketio.on('voice_command')
def handle_voice_command(data):
    """Handle voice command from browser"""
    command = data.get('command', '')
    if command:
        print(f"🎤 Voice command received from browser: {command}")
        # Process in background thread to not block WebSocket
        threading.Thread(target=process_command, args=(command,), daemon=True).start()

@socketio.on('browser_state')
def handle_browser_state(data):
    """Handle state updates from browser"""
    state = data.get('state', '')
    if state:
        print(f"📱 Browser state: {state}")
        update_orb_state(state)

def start_server():
    """Start the Flask-SocketIO server"""
    # Create templates directory if it doesn't exist
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    os.makedirs(templates_dir, exist_ok=True)
    
    print("=" * 60)
    print("🚀 Starting Zara AI Web UI Server")
    print("=" * 60)
    print("🌐 Server will be available at: http://localhost:5000")
    print("🎤 Microphone will be used for voice input")
    print("🔊 Audio will play through your default speakers")
    print("")
    print("⚠️  IMPORTANT:")
    print("   1. Make sure your microphone is connected")
    print("   2. Grant microphone permissions if prompted")
    print("   3. Open http://localhost:5000 in your browser")
    print("   4. Wait for the green orb to start speaking")
    print("")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    print("")
    
    # Start AI interaction loop in background thread
    ai_thread = threading.Thread(target=ai_interaction_loop, daemon=True)
    ai_thread.start()
    
    try:
        socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Server error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    start_server()
