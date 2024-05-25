from pydantic import BaseModel
from typing import Union

class TarefaIn(BaseModel):
    nome: str
    descricao: str
    data_prevista_conclusao: str
    funcionariosId: Union[int]

class TarefaOut(BaseModel):
    id: int
    nome: str
    descricao: str
    data_prevista_conclusao: str
