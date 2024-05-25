from src.database import conexãoBancoDados
from src.models.relatorio_model import Relatorio

def adicionarRelatorio(relatorio: Relatorio) -> bool:
    try:
        conn = conexãoBancoDados()
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
    
def getRelatoriosFuncionario(idUser: int):
    conn = conexãoBancoDados()
    cursor = conn.cursor()

    cursor.execute("""SELECT id, id_user, id_tarefa, data_criação, texto FROM Relatorios
                   WHERE id_user = ?;""", (idUser,))
    
    relatorios = []
    queryRelatorios = cursor.fetchall()

    for relatorio in queryRelatorios:
        relatorios.append({
            "id": relatorio[0],
            "id_user": relatorio[1],
            "id_tarefa": relatorio[2],
            "data_criacao": relatorio[3],
            "texto": relatorio[4]
        })
    
    conn.close()

    return relatorios
