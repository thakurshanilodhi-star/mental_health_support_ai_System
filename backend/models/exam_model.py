# Exam related data store karega

from backend.database.connection import get_connection


def save_exam(user_id, subject, exam_date, syllabus_json):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO exams (user_id, subject, exam_date, syllabus_json)
        VALUES (?, ?, ?, ?)
    """, (user_id, subject, exam_date, syllabus_json))

    conn.commit()
    conn.close()


def get_exams(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM exams WHERE user_id = ?
    """, (user_id,))

    exams = cursor.fetchall()
    conn.close()

    return exams