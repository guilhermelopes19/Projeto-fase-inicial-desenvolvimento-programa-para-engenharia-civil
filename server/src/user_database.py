from src.database import conexãoBancoDados
from src.models.user_models import UserIn, UserOut

def validarUser(user: UserIn):
    conn = conexãoBancoDados()
    cursor = conn.cursor()

    cursor.execute("SELECT username, password, tipo FROM Users WHERE username = ? AND password = ?;", (user.username, user.password))
    
    query = cursor.fetchone()
    conn.close()

    if query != None:
        return {
            "status": True,
            "user": UserOut(username=query[0], tipo=query[2])}
    
    return {
            "status": False
        }

def adicionarFuncionario(func: UserIn):
    try:
        conn = conexãoBancoDados()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO Users (username, password, tipo) VALUES
                    (?, ?, 'funcionario');""", (func.username, func.password))
        
        conn.commit()
        conn.close()

        return True
    except Exception as err:
        print(err)
        return False

def getFuncionarios():
    conn = conexãoBancoDados()
    cursor = conn.cursor()

    cursor.execute("""SELECT username FROM Users
                   WHERE tipo='funcionario';""")
    
    query = cursor.fetchall()

    conn.close()

    return query
