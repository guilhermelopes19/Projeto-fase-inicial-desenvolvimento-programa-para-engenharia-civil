from pydantic import BaseModel

class Tarefa(BaseModel):
    nome: str
    descricao: str
    data_prevista_conclusao: str
    funcionariosId: list
