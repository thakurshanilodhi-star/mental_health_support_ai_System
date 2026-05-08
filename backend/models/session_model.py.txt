# Study session related operations

from backend.database.connection import get_connection


def save_session(user_id, subject, duration):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO study_sessions (user_id, subject, duration)
        VALUES (?, ?, ?)
    """, (user_id, subject, duration))

    conn.commit()
    conn.close()


def get_sessions(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM study_sessions WHERE user_id = ?
    """, (user_id,))

    sessions = cursor.fetchall()
    conn.close()

    return sessions