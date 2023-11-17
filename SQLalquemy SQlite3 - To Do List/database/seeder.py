import sqlite3 as sql

DB_PATH = "C:\\Users\\PERSONAL\\PycharmProjects\\pythonFlask\\SQLalquemy SQlite3 - To Do List\\database\\tasks.db"

def createDB():
    # Conexión
    conn = sql.connect(DB_PATH)
    # Cursor
    cursor = conn.cursor()
    # Crear tabla
    cursor.execute("""CREATE TABLE tasks (
                content text,
                done boolean
            )""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Creating database...")
    createDB()
