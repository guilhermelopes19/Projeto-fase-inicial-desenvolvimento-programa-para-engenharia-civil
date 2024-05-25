from src.models.tarefa_models import Tarefa
from src.database import conexãoBancoDados

def adicionarTarefa(tarefa: Tarefa) -> bool:
    try:
        conn = conexãoBancoDados()
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

def getTodasTarefas() -> dict:
    conn = conexãoBancoDados()
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
        tar = cursor.fetchone()

        tarefas.append({
            "nome": tar[0],
            "descricao": tar[1],
            "data_prevista_conclusao": tar[2],
            "funcionarios": []
        })

        for funcId in value:
            cursor.execute("""SELECT username FROM Users
                           WHERE id = ?;""", (funcId,))
            funcName = cursor.fetchone()[0]
            tarefas[c]["funcionarios"].append(funcName)

        c += 1

    return tarefas
