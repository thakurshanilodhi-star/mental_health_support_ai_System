# Daily study plan store karega

from backend.database.connection import get_connection


def save_plan(user_id, date, tasks_json):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO daily_plans (user_id, date, tasks_json)
        VALUES (?, ?, ?)
    """, (user_id, date, tasks_json))

    conn.commit()
    conn.close()


def get_plans(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM daily_plans WHERE user_id = ?
    """, (user_id,))

    plans = cursor.fetchall()
    conn.close()

    return plans