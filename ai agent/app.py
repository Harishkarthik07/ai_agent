from flask import Flask, request, jsonify
from stt import transcribe_audio
from llm import generate_response
from tts import synthesize_speech
from livekit_client import start_session
from metrics import log_metrics

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def voice_interaction():
    audio_url = request.json.get("audio_url")
    transcript = transcribe_audio(audio_url)
    response = generate_response(transcript)
    audio_output_url = synthesize_speech(response)
    log_metrics(transcript, response)
    return jsonify({
        "transcript": transcript,
        "response": response,
        "audio_output_url": audio_output_url
    })

@app.route('/start_call', methods=['GET'])
def start_call():
    session_url = start_session()
    return jsonify({"session_url": session_url})

if __name__ == '__main__':
    app.run(debug=True)