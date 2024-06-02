from src.database import conexaoBancoDados
from src.models.user_model import UserIn, UserOut

# Valida o usuario no banco de dados. Recebe como argumento um objeto UserIn
def validarUser(user: UserIn) -> bool:
    conn = conexaoBancoDados()
    cursor = conn.cursor()

    cursor.execute("""SELECT id, username, password, tipo FROM Users 
                   WHERE username = ? AND password = ?;""", (user.username, user.password))
    
    query = cursor.fetchone()
    conn.close()

    if query != None:
        return {
            "status": True,
            "user": UserOut(id=query[0], username=query[1], tipo=query[3])}
    
    return {
            "status": False
        }

# Adiciona um funcionario no banco de dados. Recebe um objeto UserIn
def adicionarFuncionario(func: UserIn) -> bool:
    try:
        conn = conexaoBancoDados()
        cursor = conn.cursor()
        
        cursor.execute("""INSERT INTO Users (username, password, tipo) VALUES
                    (?, ?, 'funcionario');""", (func.username, func.password))
        
        conn.commit()
        conn.close()

        return True
    except Exception as err:
        print(err)
        return False

# Retorna uma lista de dicionarios com todos os funcionarios
def getFuncionarios() -> list:
    conn = conexaoBancoDados()
    cursor = conn.cursor()

    cursor.execute("""SELECT id, username FROM Users
                   WHERE tipo='funcionario';""")
    
    query = cursor.fetchall()
    conn.close()

    funcionarios = []
    
    for func in query:
        funcionarios.append({
                "id": func[0],
                "nome": func[1]
            })

    return funcionarios
