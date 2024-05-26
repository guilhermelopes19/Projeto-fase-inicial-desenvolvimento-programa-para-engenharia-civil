import sqlite3

def conexãoBancoDados():
    caminhoBd = "./server/database/gerenciador-tarefas.db"
    
    conn = sqlite3.connect(caminhoBd)

    return conn

async def inicializarBancoDados():
    conn = conexãoBancoDados()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL UNIQUE,
                   password TEXT,
                   tipo TEXT CHECK(tipo IN ('admin', 'funcionario')) NOT NULL DEFAULT 'funcionario'
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Tarefas(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL UNIQUE,
                   descricao TEXT NOT NULL,
                   data_prevista_conclusao TEXT
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Relatorios(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   id_user INTEGER NOT NULL,
                   id_tarefa INTEGER NOT NULL,
                   data_criação TEXT NOT NULL,
                   texto TEXT,
                   FOREIGN KEY(id_user) REFERENCES Users(id),
                   FOREIGN KEY(id_tarefa) REFERENCES Tarefas(id)
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS UserExecutarTarefa(
                   id_user INTEGER NOT NULL,
                   id_tarefa INTEGER NOT NULL,
                   FOREIGN KEY(id_user) REFERENCES Users(id),
                   FOREIGN KEY(id_tarefa) REFERENCES Tarefas(id)
    );''')

    cursor.execute("SELECT * FROM Users WHERE username = 'admin';")
    query = cursor.fetchone()
    
    if query == None:
        cursor.execute('''INSERT INTO Users (username, password, tipo) VALUES ('admin', 'admin', 'admin');''')

    conn.commit()

    print("Conexão com banco de dados bem sucedida!")
    conn.close()
