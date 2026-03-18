import sqlite3

conn = sqlite3.connect("calls.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS calls (
    company TEXT,
    objection TEXT,
    intent TEXT
)
""")

def insert(data):
    cur.execute(
        "INSERT INTO calls VALUES (?, ?, ?)",
        (data["company"], data["objection"], data["intent"])
    )
    conn.commit()