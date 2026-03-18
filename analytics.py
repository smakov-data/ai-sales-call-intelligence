import sqlite3

conn = sqlite3.connect("calls.db")
cur = conn.cursor()

print("\nTop objections:")
for row in cur.execute("""
SELECT objection, COUNT(*) 
FROM calls 
GROUP BY objection
"""):
    print(row)

print("\nIntent distribution:")
for row in cur.execute("""
SELECT intent, COUNT(*) 
FROM calls 
GROUP BY intent
"""):
    print(row)