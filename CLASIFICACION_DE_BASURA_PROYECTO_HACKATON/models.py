import sqlite3

DB_NAME = "waste_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reciclaje (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            objeto_detectado TEXT,
            categoria_predicha TEXT,
            confianza REAL,
            ruta_imagen TEXT,
            es_correcto BOOLEAN DEFAULT NULL,
            categoria_real TEXT DEFAULT NULL
        )
    ''')
    conn.commit()
    conn.close()

def guardar_registro(objeto, categoria, confianza, ruta_img):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reciclaje (objeto_detectado, categoria_predicha, confianza, ruta_imagen)
        VALUES (?, ?, ?, ?)
    ''', (objeto, categoria, confianza, ruta_img))
    last_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return last_id

def obtener_ultimo_registro():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reciclaje ORDER BY id DESC LIMIT 1')
    data = cursor.fetchone()
    conn.close()
    return data

def obtener_estadisticas():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT categoria_predicha, COUNT(*) FROM reciclaje GROUP BY categoria_predicha')
    data = cursor.fetchall()
    conn.close()
    return data

def actualizar_feedback(id_registro, es_correcto, categoria_real=None):
    """Aquí ocurre el aprendizaje humano: guardamos si la IA se equivocó"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reciclaje 
        SET es_correcto = ?, categoria_real = ?
        WHERE id = ?
    ''', (es_correcto, categoria_real, id_registro))
    conn.commit()
    conn.close()

# Inicializar al importar
init_db()