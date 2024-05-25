from pydantic import BaseModel

class Relatorio(BaseModel):
    id_user: int
    id_tarefa: int
    texto: str
    data_criacao: str
    
