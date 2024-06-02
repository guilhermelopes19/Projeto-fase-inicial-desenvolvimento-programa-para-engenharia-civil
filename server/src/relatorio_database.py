from src.database import conexaoBancoDados
from src.models.relatorio_model import Relatorio

# Adiciona um novo relatorio no banco de dados. Recebe um objeto Relatorio como argumento
def adicionarRelatorio(relatorio: Relatorio) -> bool:
    try:
        conn = conexaoBancoDados()
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO Relatorios 
                    (id_user, id_tarefa, data_criação, texto) VALUES
                    (?, ?, ?, ?);
                    """, (relatorio.id_user, relatorio.id_tarefa, relatorio.data_criacao, relatorio.texto))
            
        conn.commit()
        conn.close()

        return True
    except Exception as err:
        print(err)
        return False

# Retorna uma lista de dicionarios com os relatorios do funcionario. Recebe o id do funcionario como argumento
def getRelatoriosFuncionario(idUser: int) -> list:
    conn = conexaoBancoDados()
    cursor = conn.cursor()

    cursor.execute("""SELECT id, id_tarefa, data_criação, texto FROM Relatorios
                   WHERE id_user = ?;""", (idUser,))
    
    relatorios = []
    queryRelatorios = cursor.fetchall()

    for relatorio in queryRelatorios:
        cursor.execute("""SELECT nome FROM Tarefas
                       WHERE id = ?;""", (relatorio[1],))
        nomeTarefa = cursor.fetchone()[0]

        relatorios.append({
            "id": relatorio[0],
            "id_tarefa": relatorio[1],
            "nome_tarefa": nomeTarefa,
            "data_criacao": relatorio[2],
            "texto": relatorio[3]
        })
    
    conn.close()

    return relatorios

# Retorna uma lista de dicionarios com todos os relatorios cadastrados no sistema
def getTodosRelatorios() -> list:
    conn = conexaoBancoDados()
    cursor = conn.cursor()

    cursor.execute("""SELECT id, id_user, id_tarefa, data_criação, texto FROM Relatorios;""")
    query = cursor.fetchall()

    relatorios = []

    for relatorio in query:
        cursor.execute("""SELECT username FROM Users
                       WHERE id = ?;""", (relatorio[1],))
        nomeFunc = cursor.fetchone()[0]

        cursor.execute("""SELECT nome FROM Tarefas
                       WHERE id = ?;""", (relatorio[2],))
        nomeTarefa = cursor.fetchone()[0]

        relatorios.append({
            "id": relatorio[0],
            "id_user": relatorio[1],
            "id_tarefa": relatorio[2],
            "nome_funcionario": nomeFunc,
            "nome_tarefa": nomeTarefa,
            "data_criacao": relatorio[3],
            "texto": relatorio[4]
        })

    conn.close()

    return relatorios
