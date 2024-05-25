from pydantic import BaseModel
from typing import Union

class Tarefa(BaseModel):
    nome: str
    descricao: str
    data_prevista_conclusao: str
    funcionariosId: Union[int]
