# Global database helper (optional wrapper)

from backend.database.connection import get_connection


def execute_query(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()
    conn.close()


def fetch_all(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)
    data = cursor.fetchall()

    conn.close()
    return data