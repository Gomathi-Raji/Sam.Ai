# Zara AI - Quick Start Guide

## 🚀 Running the Web UI

### Option 1: Using Python directly
```bash
python main.py
```

### Option 2: Using the startup script
```bash
./start_web_ui.sh
```

### Option 3: Terminal mode (if you want the old behavior)
```bash
python main.py --terminal
```

## 🌐 Accessing the Interface

Once the server starts, you'll see:
```
🌐 Starting Zara Web UI Server...
🌐 Open http://localhost:5000 in your browser
```

Open your browser and navigate to:
**http://localhost:5000**

## 🎨 Understanding the Orb States

### 🔵 Blue (Ready)
- **What it means**: Zara is idle and ready to listen
- **Animation**: Gentle floating motion
- **What to do**: Wait for the next listening cycle

### 🟢 Green (Listening)
- **What it means**: Zara is actively listening for your voice command
- **Animation**: Pulsing green glow
- **What to do**: **Speak your command clearly now!**

### 🟣 Purple (Processing)
- **What it means**: Zara is processing your request with AI
- **Animation**: Rotating purple pulse
- **What to do**: Wait for the response

### 🔴 Red/Orange (Speaking)
- **What it means**: Zara is speaking the response
- **Animation**: Strong pulsing red/orange
- **What to do**: Listen to the response

## 🎤 Voice Commands

Zara understands all the same commands as the terminal version:

### Music Commands
- "Play song" - Then say the song name
- "Play [song name]" - Directly play a song
- "Play music"
- "Spotify"

### General Commands
- Ask questions (powered by Gemini AI)
- Request tasks
- General conversation

## 🔧 Troubleshooting

### Server won't start
```bash
# Check if port 5000 is in use
lsof -i :5000

# If something is using it, kill it or use a different port
# Edit web_ui.py and change the port number
```

### Can't hear audio
- Check your system audio settings
- Ensure speakers/headphones are connected
- Check microphone permissions

### Microphone not working
- Grant microphone permissions to your browser
- Check that your microphone is set as default input device
- Test with: `python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"`

### Orb not animating
- Check browser console (F12) for errors
- Ensure WebSocket connection is established
- Try refreshing the page

### AI not responding
- Check your Gemini API key in `config.py`
- Verify internet connection
- Check console for error messages

## 📊 Checking Logs

Conversations are logged to:
```
/workspaces/Sam.Ai/conversation_log.txt
```

View recent logs:
```bash
tail -f /workspaces/Sam.Ai/conversation_log.txt
```

## 🛑 Stopping the Server

Press `Ctrl+C` in the terminal where the server is running

## 🎯 Tips for Best Experience

1. **Speak clearly** when the orb is green (listening)
2. **Wait for the cycle** - Don't interrupt during speaking/processing
3. **Use a quiet environment** for best voice recognition
4. **Keep browser window open** - Don't minimize it
5. **Use Chrome/Edge** for best compatibility

## 🔄 Restarting the Server

If you encounter issues:
```bash
# Stop the server (Ctrl+C)
# Then restart:
python main.py
```

## 📱 Access from Other Devices

The server runs on `0.0.0.0`, so you can access it from other devices on your network:

1. Find your computer's IP address:
   ```bash
   hostname -I
   ```

2. On another device, open browser to:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```

## 🎨 Customizing the Orb

Edit `templates/orb_ui.html` to customize:
- Colors (search for `rgba()` values)
- Size (change `width` and `height` in `.orb` class)
- Animation speed (change animation durations)

See `WEB_UI_README.md` for detailed customization guide.

## 📞 Support

If you encounter issues:
1. Check the console output for errors
2. Review the logs in `conversation_log.txt`
3. Run the test script: `python test_web_ui_setup.py`
4. Ensure all dependencies are installed: `pip install -r requirements.txt`

---

**Enjoy your new Zara AI Web UI! 🎉**
