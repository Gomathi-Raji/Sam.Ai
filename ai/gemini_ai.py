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

    # Simple rule-based responses
    if any(word in prompt_lower for word in ["hello", "hi", "வணக்கம்", "ஹலோ"]):
        return "வணக்கம்! நான் ஜாரா. உங்களுக்கு எப்படி உதவ முடியும்?"

    elif any(word in prompt_lower for word in ["how are you", "எப்படி இருக்கிறாய்"]):
        return "நான் நன்றாக இருக்கிறேன்! நீங்கள் எப்படி இருக்கிறீர்கள்?"

    elif any(word in prompt_lower for word in ["what is your name", "உன் பெயர் என்ன"]):
        return "என் பெயர் ஜாரா. நான் உங்கள் AI உதவியாளர்."

    elif any(word in prompt_lower for word in ["thank you", "thanks", "நன்றி"]):
        return "நன்றி! உங்களுக்கு மேலும் உதவ வேண்டுமா?"

    elif any(word in prompt_lower for word in ["bye", "goodbye", "பிரியாவிடை"]):
        return "பிரியாவிடை! மீண்டும் சந்திப்போம்."

    elif any(word in prompt_lower for word in ["play", "music", "song", "பாடல்", "இசை"]):
        return "நீங்கள் எந்த பாடலை கேட்க விரும்புகிறீர்கள்? பாடல் பெயரை சொல்லுங்கள்."

    else:
        # Generic fallback
        return "மன்னிக்கவும், நான் தற்போது சிறிது பிஸியாக இருக்கிறேன். சிறிது நேரம் கழித்து மீண்டும் முயற்சிக்கவும்."