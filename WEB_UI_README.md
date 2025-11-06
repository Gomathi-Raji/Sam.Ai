# Zara AI - Web UI with Orb Visualization

## Overview
This is a modern web-based interface for Zara AI that features a beautiful animated orb visualization that syncs with the AI's listening and speaking states.

## Features
- **Orb Visualization**: Beautiful animated orb that changes color and animation based on AI state
  - 🔵 Blue (Ready): Idle state, gently floating
  - 🟢 Green (Listening): Actively listening to user input
  - 🔴 Red (Speaking): AI is speaking/responding
  - 🟣 Purple (Processing): AI is processing the request

- **Real-time State Sync**: WebSocket connection ensures the orb animation is perfectly synced with the AI's actual state
- **No Text Clutter**: Clean, minimalist interface with only the orb visualization
- **Voice Interaction**: All interactions happen through voice, just like the terminal version

## How It Works

### Architecture
1. **Flask Backend** (`web_ui.py`): Handles WebSocket connections and AI interaction
2. **HTML/CSS Frontend** (`templates/orb_ui.html`): Pure CSS orb with smooth animations
3. **WebSocket Communication**: Real-time state updates between backend and frontend

### Running the Web UI

**Default mode (Web UI):**
```bash
python main.py
```

**Terminal mode (if needed):**
```bash
python main.py --terminal
```

### Access the Interface
Once started, open your browser to:
```
http://localhost:5000
```

## States Explained

### Ready State (Blue)
- Default idle state
- Gentle floating animation
- Waiting for voice command

### Listening State (Green)
- Activated when the AI is listening for your voice
- Pulsing animation indicates active listening
- Speak your command clearly

### Processing State (Purple)
- AI is processing your request
- Rotating pulse animation
- Getting response from Gemini AI

### Speaking State (Red)
- AI is speaking the response
- Strong pulsing animation synced with speech
- Listen to the AI's response

## Customization

### Changing Colors
Edit the CSS gradients in `templates/orb_ui.html`:

```css
.orb.ready {
    background: radial-gradient(circle at 30% 30%, 
        rgba(100, 150, 255, 0.8),  /* Change these RGB values */
        rgba(50, 100, 200, 0.6), 
        rgba(20, 50, 150, 0.3));
}
```

### Changing Animation Speed
Modify the animation duration in the CSS:

```css
animation: pulse-listening 1.5s ease-in-out infinite;
                        /* ^ Change this value */
```

### Changing Orb Size
Edit the width and height in the `.orb` class:

```css
.orb {
    width: 300px;  /* Change size here */
    height: 300px;
}
```

## Technical Details

### WebSocket Events
- `connect`: Client connects to server
- `disconnect`: Client disconnects
- `state_change`: Server broadcasts state changes to all clients
- `manual_command`: (Optional) Send text commands from UI

### Server Configuration
Default settings in `web_ui.py`:
- Host: `0.0.0.0` (accessible from network)
- Port: `5000`
- CORS: Enabled for all origins

## Troubleshooting

### Orb not animating
- Check browser console for WebSocket connection errors
- Ensure Flask server is running
- Check network/firewall settings

### Audio not working
- Ensure microphone permissions are granted
- Check that `pyaudio` is properly installed
- Verify microphone is selected as default input device

### Server won't start
- Check if port 5000 is already in use
- Install missing dependencies: `pip install -r requirements.txt`
- Check for Python version compatibility (3.7+)

## Dependencies
- Flask: Web server
- Flask-SocketIO: WebSocket support
- All existing Zara AI dependencies (voice, AI, etc.)

## Performance
- Very lightweight - pure CSS animations (no Canvas/WebGL overhead)
- Real-time WebSocket updates with minimal latency
- Works smoothly on low-end devices and mobile browsers

## Browser Support
- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Mobile browsers: ✅ Works well

## Future Enhancements
- Audio waveform visualization
- Multiple orb themes
- Touch/click interactions
- Dark/light mode toggle
- Mobile app wrapper
