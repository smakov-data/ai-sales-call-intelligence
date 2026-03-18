import json
import re

from prompts import PROMPT
from llm import call_llm
from db import insert


def normalize_objection(text):
    text = text.lower()

    if "not interested" in text:
        return "no_interest"
    if "price" in text:
        return "price"
    if "time" in text or "timing" in text:
        return "timing"
    if "quality" in text:
        return "quality"

    return text


def safe_parse(raw):
    try:
        match = re.search(r"\{.*?\}", raw, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        pass

    return {
        "company": "unknown",
        "objection": "unknown",
        "intent": "neutral"
    }


def process(transcript):
    prompt = PROMPT.format(transcript=transcript)
    raw = call_llm(prompt)

    data = safe_parse(raw)

    data["objection"] = normalize_objection(data["objection"])
    data["intent"] = data["intent"].lower()

    insert(data)

    return data


def pretty_print(data):
    print("\n📊 RESULT")
    print("-" * 30)
    print(f"Company   : {data['company']}")
    print(f"Objection : {data['objection']}")
    print(f"Intent    : {data['intent']}")

if __name__ == "__main__":
    calls = [
        "Client ABC Corp says price is too high but interested",
        "XYZ Inc not interested, timing is bad",
        "Company QWE worried about quality",
    ]

    for c in calls:
        result = process(c)
        pretty_print(result)