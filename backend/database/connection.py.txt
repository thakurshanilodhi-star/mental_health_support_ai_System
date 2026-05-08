# Ye file database connection handle karegi

import sqlite3

# Database file ka naam
DB_NAME = "academic_ai.db"

def get_connection():
    """
    Ye function database se connection banata hai
    Har model isi function ko use karega
    """
    conn = sqlite3.connect(DB_NAME)
    
    # Row ko dictionary jaisa access karne ke liye
    conn.row_factory = sqlite3.Row
    
    return conn