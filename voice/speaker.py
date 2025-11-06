from gtts import gTTS
import pygame
import os

def speak(text):
    print(f"🤖 zara (Tamil): {text}")

    # Check if we're in a container environment (no audio device)
    try:
        # Try to initialize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load("voice.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        pygame.mixer.quit()
        os.remove("voice.mp3")
    except Exception as e:
        # In container environments, audio won't work
        # This is expected - browser TTS will handle the audio
        print(f"⚠️ Audio playback not available (container environment): {e}")
        print("   Using browser-based text-to-speech instead")

    # Note: TTS file generation is handled by browser now
    # We keep this for potential future use or local testing
