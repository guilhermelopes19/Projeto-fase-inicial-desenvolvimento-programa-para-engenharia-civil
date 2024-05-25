from src.database import conexãoBancoDados
from src.models.relatorio_model import Relatorio

def adicionarRelatorio(relatorio: Relatorio) -> bool:
    try:
        conn = conexãoBancoDados()
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO Relatorios 
                    (id_user, id_tarefa, data_criacao, texto) VALUES
                    (?, ?, ?, ?);
                    """, (relatorio.id_user, relatorio.id_tarefa, relatorio.data_criacao, relatorio.texto))
            
        conn.commit()
        conn.close()

        return True
    except Exception as err:
        print(err)
        return False
