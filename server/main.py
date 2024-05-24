from fastapi import FastAPI, HTTPException, status
import uvicorn
from contextlib import asynccontextmanager 
from src.user_models import UserIn
from src import database

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.inicializarBancoDados()
    yield

app.router.lifespan_context = lifespan

@app.post("/auth")
async def autenticar_user(user: UserIn):
    validarUser = database.validarUser(user=user)

    if validarUser.get("status"):
        return validarUser.get("user")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado!"
        )

@app.put("/admin/funcionario", status_code=status.HTTP_201_CREATED)
async def adicionar_funcionario(func: UserIn):
    if database.adicionarFuncionario(func=func):
        return "Funcionario Adicionado com Sucesso!"
    else:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="Erro ao adicionar novo funcionario!"
        )

@app.get("/admin/funcionario")
async def lista_funcionarios():
    return database.getFuncionarios()

if __name__ == "__main__":
    uvicorn.run(app=app)
