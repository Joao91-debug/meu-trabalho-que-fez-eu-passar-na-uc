import sqlite3

DATABASE = 'feedback.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedbacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_atendente TEXT NOT NULL,
            setor TEXT NOT NULL,
            tipo_atendimento TEXT NOT NULL,
            nota REAL NOT NULL,
            classificacao TEXT NOT NULL,
            comentario TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_feedback(nome_atendente, setor, tipo_atendimento, nota, classificacao, comentario):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO feedbacks (nome_atendente, setor, tipo_atendimento, nota, classificacao, comentario)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome_atendente, setor, tipo_atendimento, nota, classificacao, comentario))
    conn.commit()
    conn.close()

def get_all_feedbacks():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM feedbacks')
    feedbacks = cursor.fetchall()
    conn.close()
    return feedbacks

if __name__ == '__main__':
    init_db()
    print("Banco de dados 'feedback.db' inicializado com sucesso!")