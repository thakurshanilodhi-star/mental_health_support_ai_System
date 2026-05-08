# Ye file saare tables create karegi
# Sirf ek baar run karna hai

from backend.database.connection import get_connection

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # ---------------- USERS TABLE ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        language TEXT NOT NULL,
        persona TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ---------------- STUDY SESSIONS TABLE ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS study_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subject TEXT,
        duration INTEGER,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ---------------- REFLECTION TABLE ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reflections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER,
        focus_score INTEGER,
        distraction_count INTEGER,
        clarity_level TEXT,
        next_action TEXT,
        FOREIGN KEY(session_id) REFERENCES study_sessions(id)
    )
    """)

    # ---------------- DAILY PLANS TABLE ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_plans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT,
        tasks_json TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

    print("Tables created successfully.")