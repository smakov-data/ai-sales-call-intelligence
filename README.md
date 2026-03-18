# AI Sales Call Intelligence

## Overview
This project demonstrates an end-to-end AI pipeline for extracting structured business insights from unstructured sales call transcripts using a local LLM (phi3).

The system converts raw conversation text into actionable data such as:
- Company name
- Customer objections
- Intent (interested / not_interested / neutral)

---

## Architecture

Input (call transcript)
→ LLM (phi3 via API)
→ JSON extraction
→ Normalization layer
→ SQLite storage
→ Analytics

---

## Pipeline Flow

1. Raw transcript is passed to LLM
2. LLM returns semi-structured JSON (often noisy)
3. Parser extracts valid JSON
4. Data is normalized (e.g. "price is too high" → "price")
5. Data is stored in SQLite
6. Analytics layer aggregates insights

---

## Example

### Input
