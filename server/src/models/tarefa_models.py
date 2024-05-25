from pydantic import BaseModel

class TarefaIn(BaseModel):
    nome: str
    descricao: str
    data_prevista_conclusao: str
    funcionariosId: list

class TarefaOut(BaseModel):
    id: int
    nome: str
    descricao: str
    data_prevista_conclusao: str
