# Ye file user se related database operations handle karegi

from backend.database.connection import get_connection


def create_user(name, language, persona):
    """
    Naya user database me add karega
    """

    # Database connection open karo
    conn = get_connection()
    cursor = conn.cursor()

    # User insert query
    cursor.execute("""
        INSERT INTO users (name, language, persona)
        VALUES (?, ?, ?)
    """, (name, language, persona))

    # Changes save karo
    conn.commit()

    # Connection close karo
    conn.close()


def get_user(user_id):
    """
    Database se ek specific user fetch karega
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    conn.close()

    return user


def get_all_users():
    """
    Sabhi users fetch karega
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return users# Ye file user related database operations handle karegi

from backend.database.connection import get_connection

def create_user(name, language, persona):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (name, language, persona)
        VALUES (?, ?, ?)
    """, (name, language, persona))

    conn.commit()
    conn.close()


def get_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    conn.close()

    return user