from src.models.tarefa_models import TarefaIn
from src.database import conexãoBancoDados

def adicionarTarefa(tarefa: TarefaIn) -> bool:
    try:
        conn = conexãoBancoDados()
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO Tarefas 
                    (nome, descricao, data_prevista_conclusao) VALUES
                    (?, ?, ?)
                    """, (tarefa.nome, tarefa.descricao, tarefa.data_prevista_conclusao))
        conn.commit()

        cursor.execute("""SELECT id FROM Tarefas
                        WHERE nome=?""", (tarefa.nome,))
        
        id_tarefa = cursor.fetchone()[0]

        for func in tarefa.funcionariosId:
            cursor.execute("""INSERT INTO UserExecutarTarefa
                        (id_user, id_tarefa) VALUES
                        (?, ?)""", (func, id_tarefa))
            conn.commit()

        conn.close()

        return True
    except Exception as err:
        print(err)
        return False
    