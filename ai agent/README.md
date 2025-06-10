# Voice AI Agent (proPAL AI Internship Project)

This project demonstrates a real-time voice AI agent backend using:

- Flask (Backend)
- Deepgram (Speech-to-Text)
- OpenAI/Groq (LLM)
- ElevenLabs (Text-to-Speech)
- LiveKit (Call Integration Stub)
- Excel-based metric logging

## Setup

1. Clone the repo and navigate to the folder.

2. Install dependencies:
```
pip install flask openai pandas requests openpyxl
```

3. Set your API keys in the respective Python files or use `.env` + `python-dotenv`.

4. Run the app:
```
python app.py
```

## API Endpoints

- `POST /voice`: Takes audio URL, returns transcript + generated speech URL
- `GET /start_call`: Returns LiveKit session stub

## Metrics

Interaction metrics are logged to `call_logs.xlsx`.