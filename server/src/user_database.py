from src.database import conexãoBancoDados
from src.models.user_model import UserIn, UserOut

def validarUser(user: UserIn):
    conn = conexãoBancoDados()
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, password, tipo FROM Users WHERE username = ? AND password = ?;", (user.username, user.password))
    
    query = cursor.fetchone()
    conn.close()

    if query != None:
        return {
            "status": True,
            "user": UserOut(id=query[0], username=query[1], tipo=query[3])}
    
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

    funcionarios = []
    
    for func in query:
        funcionarios.append(func[0])

    return funcionarios
