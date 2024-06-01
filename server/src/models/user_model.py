from pydantic import BaseModel

# Classe que gerencia a entrada dos dados do usuario
class UserIn(BaseModel):
    username: str
    password: str

# Classe que gerencia a saida dos dados do usuario
class UserOut(BaseModel):
    id: int
    username: str
    tipo: str
