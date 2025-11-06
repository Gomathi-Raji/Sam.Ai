from config import get_model
import re
import time
from threading import Lock

# Rate limiting
last_request_time = 0
rate_limit_lock = Lock()
MIN_REQUEST_INTERVAL = 2  # seconds between requests

def clean_response(text):
    # Remove leading bullet characters like "*", "-", etc.
    cleaned_lines = []
    for line in text.splitlines():
        cleaned_line = re.sub(r"^\s*[\\-\•]\s", "", line)  # removes leading bullets with optional whitespace
        cleaned_lines.append(cleaned_line)
    return "\n".join(cleaned_lines)

def get_response(prompt):
    global last_request_time

    # Rate limiting
    with rate_limit_lock:
        current_time = time.time()
        if current_time - last_request_time < MIN_REQUEST_INTERVAL:
            print("⏳ Rate limiting - using fallback response")
            return get_fallback_response(prompt)
        last_request_time = current_time

    try:
        model = get_model()
        response = model.generate_content(prompt)
        return clean_response(response.text)
    except Exception as e:
        error_msg = str(e).lower()

        # Handle quota/rate limit errors
        if "quota exceeded" in error_msg or "rate limit" in error_msg or "429" in error_msg:
            print("⚠️ Gemini API quota exceeded - using fallback response")
            return get_fallback_response(prompt)

        # Handle other API errors
        print(f"❌ Gemini API error: {e}")
        return get_fallback_response(prompt)

def get_fallback_response(prompt):
    """Fallback responses when Gemini API is unavailable"""
    prompt_lower = prompt.lower()

    # Greetings
    if any(word in prompt_lower for word in ["hello", "hi", "வணக்கம்", "ஹலோ", "hey"]):
        return "வணக்கம்! நான் ஜாரா. உங்களுக்கு எப்படி உதவ முடியும்?"

    # Well-being
    elif any(word in prompt_lower for word in ["how are you", "எப்படி இருக்கிறாய்", "how do you do", "நீ எப்படி இருக்கிறாய்"]):
        return "நான் நன்றாக இருக்கிறேன்! நீங்கள் எப்படி இருக்கிறீர்கள்?"

    # Name queries
    elif any(word in prompt_lower for word in ["what is your name", "உன் பெயர் என்ன", "who are you", "நீ யார்"]):
        return "என் பெயர் ஜாரா. நான் உங்கள் AI உதவியாளர்."

    # Gratitude
    elif any(word in prompt_lower for word in ["thank you", "thanks", "நன்றி", "மிக்க நன்றி"]):
        return "நன்றி! உங்களுக்கு மேலும் உதவ வேண்டுமா?"

    # Farewell
    elif any(word in prompt_lower for word in ["bye", "goodbye", "பிரியாவிடை", "சந்திப்போம்", "see you"]):
        return "பிரியாவிடை! மீண்டும் சந்திப்போம்."

    # Music/Songs
    elif any(word in prompt_lower for word in ["play", "music", "song", "பாடல்", "இசை", "spotify"]):
        return "நீங்கள் எந்த பாடலை கேட்க விரும்புகிறீர்கள்? பாடல் பெயரை சொல்லுங்கள்."

    # Time queries
    elif any(word in prompt_lower for word in ["time", "clock", "நேரம்", "என்ன நேரம்"]):
        import datetime
        now = datetime.datetime.now()
        return f"தற்போதைய நேரம்: {now.strftime('%I:%M %p')}"

    # Date queries
    elif any(word in prompt_lower for word in ["date", "today", "day", "தேதி", "இன்று"]):
        import datetime
        now = datetime.datetime.now()
        return f"இன்றைய தேதி: {now.strftime('%B %d, %Y')}"

    # Weather (basic response)
    elif any(word in prompt_lower for word in ["weather", "வானிலை", "climate", "temperature"]):
        return "மன்னிக்கவும், வானிலை தகவல் தற்போது கிடைக்கவில்லை. பிறகு முயற்சிக்கவும்."

    # Help/Capabilities
    elif any(word in prompt_lower for word in ["help", "what can you do", "capabilities", "உதவி", "என்ன செய்ய முடியும்"]):
        return "நான் உங்களுக்கு பாடல்கள் இசைக்க, நேரம் சொல்ல, உரையாடல் நடத்த முடியும். எது வேண்டும்?"

    # General conversation starters
    elif any(word in prompt_lower for word in ["tell me", "சொல்லு", "what about", "என்ன நினைக்கிறாய்"]):
        return "நீங்கள் என்ன தெரிந்து கொள்ள விரும்புகிறீர்கள்? தயவுசெய்து மேலும் குறிப்பிட்டு சொல்லுங்கள்."

    # Yes/No responses
    elif prompt_lower in ["yes", "yeah", "ஆம்", "சரி", "ok", "okay"]:
        return "சரி! எது வேண்டும் சொல்லுங்கள்."
    
    elif prompt_lower in ["no", "nope", "இல்லை", "வேண்டாம்"]:
        return "சரி, வேறு ஏதாவது வேண்டுமா?"

    else:
        # Generic fallback with helpful hint
        return "மன்னிக்கவும், நான் தற்போது விரிவான பதில்கள் கொடுக்க முடியாது. நீங்கள் பாடல் இசைக்க, நேரம் தெரிந்து கொள்ள, அல்லது எளிய கேள்விகள் கேட்கலாம்."