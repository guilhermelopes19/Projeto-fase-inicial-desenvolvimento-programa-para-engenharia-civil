from src.models.tarefa_model import Tarefa
from src.database import conexaoBancoDados

# Adiciona uma nova tarefa no banco de dados. Recebe como argumento um objeto Tarefa
def adicionarTarefa(tarefa: Tarefa) -> bool:
    try:
        conn = conexaoBancoDados()
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO Tarefas 
                    (nome, descricao, data_prevista_conclusao) VALUES
                    (?, ?, ?);
                    """, (tarefa.nome, tarefa.descricao, tarefa.data_prevista_conclusao))

        cursor.execute("""SELECT id FROM Tarefas
                        WHERE nome=?;""", (tarefa.nome,))
        
        id_tarefa = cursor.fetchone()[0]

        for func in tarefa.funcionariosId:
            cursor.execute("""INSERT INTO UserExecutarTarefa
                        (id_user, id_tarefa) VALUES
                        (?, ?);""", (func, id_tarefa))
            
        conn.commit()
        conn.close()

        return True
    except Exception as err:
        print(err)
        return False

# Retorna uma lista de dicionarios com todas as tarefas cadastradas no banco de dados
def getTodasTarefas() -> list:
    conn = conexaoBancoDados()
    cursor = conn.cursor()
    tarefasId = {}
    tarefas = []

    cursor.execute("""SELECT * FROM UserExecutarTarefa;""")
    relacaoUserTarefa = cursor.fetchall()
    
    for rel in relacaoUserTarefa:
        if rel[1] in tarefasId:
            tarefasId[rel[1]].append(rel[0])
        else:
            tarefasId[rel[1]] = [rel[0]]

    c = 0
    for key, value in tarefasId.items():
        cursor.execute("""SELECT nome, descricao, data_prevista_conclusao FROM Tarefas
                       WHERE id = ?;""", (key,))
        tarefa = cursor.fetchone()

        tarefas.append({
            "id": key,
            "nome": tarefa[0],
            "descricao": tarefa[1],
            "data_prevista_conclusao": tarefa[2],
            "funcionarios": []
        })

        for funcId in value:
            cursor.execute("""SELECT username FROM Users
                           WHERE id = ?;""", (funcId,))
            funcName = cursor.fetchone()[0]
            tarefas[c]["funcionarios"].append(funcName)

        c += 1

    conn.close()
    return tarefas

# Retorna uma lista de dicionario com todas as tarefas do funcionario. Recebe o id do funcionario como argumento
def getTarefasFuncionario(idUser: int) -> list:
    conn = conexaoBancoDados()
    cursor = conn.cursor()

    cursor.execute("""SELECT id_tarefa FROM UserExecutarTarefa
                   WHERE id_user = ?;""", (idUser,))
    idTarefas = cursor.fetchall()
    tarefas = []
    c = 0

    while c < len(idTarefas):
        cursor.execute("""SELECT * FROM Tarefas
                       WHERE id = ?;""", (idTarefas[c][0],))
        tarefa = cursor.fetchall()
        
        tarefas.append({
            "id": tarefa[0][0],
            "nome": tarefa[0][1],
            "descricao": tarefa[0][2],
            "data_prevista_conclusao": tarefa[0][3]
        })

        c += 1

    conn.close()

    return tarefas
