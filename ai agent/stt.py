import requests

def transcribe_audio(audio_url):
    DEEPGRAM_API_KEY = "your_deepgram_api_key"
    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        "https://api.deepgram.com/v1/listen",
        headers=headers,
        json={"url": audio_url}
    )
    transcript = response.json()["results"]["channels"][0]["alternatives"][0]["transcript"]
    return transcript