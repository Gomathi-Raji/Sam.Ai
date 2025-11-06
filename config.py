import google.generativeai as genai
import os

# Configure Gemini API key from environment variable
api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")
genai.configure(api_key=api_key)

def get_model():
    return genai.GenerativeModel("gemini-2.0-flash-exp")

# --- Spotify API Configuration ---
# Get these credentials from https://developer.spotify.com/dashboard/
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = "http://localhost:8080/callback"

if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
    raise ValueError("SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables must be set")

# Instructions:
# 1. Go to https://developer.spotify.com/dashboard/
# 2. Create a new app
# 3. Copy the Client ID and Client Secret
# 4. Add http://localhost:8888/callback to Redirect URIs
# 5. Replace the values above with your actual credentials
