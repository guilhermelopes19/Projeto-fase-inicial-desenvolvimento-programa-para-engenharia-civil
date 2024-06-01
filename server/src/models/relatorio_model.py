from pydantic import BaseModel

# Classe que gerencia a entrada de um novo relatorio
class Relatorio(BaseModel):
    id_user: int
    id_tarefa: int
    texto: str
    data_criacao: str
