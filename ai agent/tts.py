import requests

def synthesize_speech(text):
    ELEVENLABS_API_KEY = "your_elevenlabs_api_key"
    voice_id = "your_voice_id"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    response = requests.post(url, headers=headers, json=data)
    output_path = "/mnt/data/output.mp3"
    with open(output_path, "wb") as f:
        f.write(response.content)
    return output_path