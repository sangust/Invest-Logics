import psycopg
from app.db.connection import get_conn #import da pasta db connection para conectar no banco de dados postgresql


def create_user(email, password_hash):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(''' 
                    INSERT INTO Users (email, password_hash)
                    VALUES(%s,%s)
                    ''', (email, password_hash))


    conn.commit()
    cursor.close()
    conn.close()

def login_user(email):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT password_hash FROM Users
                    WHERE email = %s''', (email,))
    
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user
    