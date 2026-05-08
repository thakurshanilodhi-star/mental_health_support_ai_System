# Reflection data store karega

from backend.database.connection import get_connection


def save_reflection(session_id, focus_score, distraction_count, clarity_level, next_action):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO reflections 
        (session_id, focus_score, distraction_count, clarity_level, next_action)
        VALUES (?, ?, ?, ?, ?)
    """, (session_id, focus_score, distraction_count, clarity_level, next_action))

    conn.commit()
    conn.close()


def get_reflections():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reflections")
    data = cursor.fetchall()

    conn.close()
    return data