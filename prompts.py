PROMPT = """
Extract structured data from sales call transcript.

Return ONLY JSON:
{{
  "company": "string",
  "objection": "string",
  "intent": "interested | not_interested | neutral"
}}

Text:
{transcript}
"""