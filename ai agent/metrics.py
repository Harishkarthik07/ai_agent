import pandas as pd
from datetime import datetime

def log_metrics(transcript, response):
    df = pd.DataFrame([{
        "timestamp": datetime.now().isoformat(),
        "transcript": transcript,
        "response": response,
        "eou_delay": 0.6,
        "ttft": 0.8,
        "ttfb": 0.5,
        "latency": 1.9
    }])
    file_path = "/mnt/data/call_logs.xlsx"
    try:
        existing = pd.read_excel(file_path)
        df = pd.concat([existing, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_excel(file_path, index=False)