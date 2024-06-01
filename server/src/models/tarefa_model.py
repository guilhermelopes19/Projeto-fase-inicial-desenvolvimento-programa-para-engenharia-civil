from pydantic import BaseModel

# Classe que gerencia a entrada de uma nova tarefa
class Tarefa(BaseModel):
    nome: str
    descricao: str
    data_prevista_conclusao: str
    funcionariosId: list
