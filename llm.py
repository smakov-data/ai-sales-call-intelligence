import requests

def call_llm(prompt: str):
    r = requests.post(
        "http://192.168.1.1:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    #print("STATUS:", r.status_code) - debug data /off

    return r.json()["response"]