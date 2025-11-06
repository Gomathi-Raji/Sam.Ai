# Using Zara AI on Your Phone 📱

## How It Works

The web UI now uses **browser-based voice recognition** which means:
- ✅ Your phone's microphone is used directly in the browser
- ✅ No need for server-side audio hardware
- ✅ Works perfectly in cloud/container environments
- ✅ Voice commands are sent to the AI server for processing

## Step-by-Step Setup

### 1. Start the Server
On your computer/codespace:
```bash
python main.py
```

You should see:
```
🌐 Server will be available at: http://localhost:5000
📱 Voice recognition will happen in the browser (on your phone)
```

### 2. Find Your Server IP

If accessing from your phone (not the same device):
```bash
hostname -I
```

Example output: `192.168.1.100`

### 3. Open on Your Phone

**Option A: Same Device**
```
http://localhost:5000
```

**Option B: Different Device (Phone on same WiFi)**
```
http://YOUR_IP_ADDRESS:5000
```
Example: `http://192.168.1.100:5000`

**Option C: Codespace/Dev Container**
The port should be automatically forwarded. Check the "PORTS" tab in VS Code and click the globe icon next to port 5000.

### 4. Grant Microphone Permission

When the page loads, your browser will ask:
```
Allow microphone access?
```

✅ **Click "Allow"** - This is essential!

### 5. Start Talking!

The orb will automatically start listening. You'll see:

- 🟢 **Green Orb**: Speak now! The browser is listening
- 🟣 **Purple Orb**: AI is processing your command
- 🔴 **Red Orb**: AI is speaking (listen to response)
- 🔵 **Blue Orb**: Ready/Idle

## Voice Commands

Speak clearly in Tamil or English:

### Examples:
- "What is the weather?" (English)
- "என்ன செய்கிறாய்?" (Tamil - What are you doing?)
- "Play music" (then say song name)
- "Tell me a joke"
- Any question you'd ask an AI

## Troubleshooting

### No Green Orb / Not Listening

**Check:**
1. Did you allow microphone permission?
2. Are you using Chrome or Edge browser?
3. Check browser console (3-dot menu → More tools → Developer tools → Console)

**Fix:**
- Refresh the page
- Click the orb manually to trigger listening
- Check microphone permissions in browser settings

### Orb Stays Blue

**Possible causes:**
- Microphone permission denied
- Browser doesn't support Speech Recognition
- No internet connection

**Fix:**
- Use Chrome or Edge on Android
- Use Safari on iOS
- Grant microphone permission
- Check internet connection

### Commands Not Working

**Check:**
- Speak clearly and wait for the orb to turn green
- Make sure you're speaking Tamil (ta-IN) or switch language if needed
- Check the browser console for errors
- Make sure the server is still running

### Audio Not Playing

**Note:** The current setup plays audio on the **server**, not the phone.

To hear responses on your phone, you need to:
1. Be using headphones/speakers connected to the server
2. OR we can add browser-based text-to-speech (see below)

## Advanced: Browser-Based Audio

If you want to hear responses on your phone, open the browser developer console and check if audio is being sent. We can add browser-based TTS if needed.

## Browser Compatibility

| Browser | Android | iOS | Desktop |
|---------|---------|-----|---------|
| Chrome  | ✅      | ❌  | ✅      |
| Edge    | ✅      | ❌  | ✅      |
| Safari  | ❌      | ✅  | ✅      |
| Firefox | ⚠️      | ❌  | ⚠️      |

✅ = Fully supported
⚠️ = Partial support
❌ = Not supported

## Tips for Best Experience

1. **Use headphones** to avoid echo/feedback
2. **Speak clearly** and wait for green orb
3. **One command at a time** - wait for response before next command
4. **Quiet environment** - reduce background noise
5. **Keep phone screen on** - some browsers pause when screen is off
6. **Stable internet** - required for both voice recognition and AI processing

## Click to Start

If listening doesn't auto-start:
- **Tap the orb** to manually trigger listening
- You should see it turn green and browser should ask for mic permission

## Checking What's Happening

Open browser console to see logs:
1. Tap 3 dots (⋮) in browser
2. Go to "Developer tools" or "More tools"
3. Select "Console" tab

You should see messages like:
```
✅ Connected to Zara AI server
🎤 Browser listening started
📝 Heard: your command here
```

## Port Forwarding for Codespaces

If using GitHub Codespaces:
1. Go to "PORTS" tab in VS Code
2. Find port 5000
3. Change visibility to "Public"
4. Click the globe icon to get public URL
5. Open that URL on your phone

## Security Note

If making the port public, anyone with the URL can access your AI assistant. Only share with trusted devices.

---

**Now you can use Zara AI from anywhere using just your phone! 🎉**
