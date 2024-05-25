from fastapi import FastAPI, HTTPException, status
import uvicorn
from contextlib import asynccontextmanager 
from src import database, user_database, tarefa_database
from src.models.user_models import UserIn
from src.models.tarefa_models import TarefaIn

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.inicializarBancoDados()
    yield

app.router.lifespan_context = lifespan

@app.post("/auth")
async def autenticar_user(user: UserIn):
    validarUser = user_database.validarUser(user=user)

    if validarUser.get("status"):
        return validarUser.get("user")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado!"
        )

@app.put("/admin/funcionario")
async def adicionar_funcionario(func: UserIn):
    if user_database.adicionarFuncionario(func=func):
        return "Funcionario Adicionado com Sucesso!"
    else:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Erro ao adicionar novo funcionario!"
        )

@app.get("/admin/funcionario")
async def lista_funcionarios():
    return user_database.getFuncionarios()

@app.put("/admin/tarefa")
async def adicionar_tarefa(tarefa: TarefaIn):
    if tarefa_database.adicionarTarefa(tarefa=tarefa):
        return "Tarefa adicionada com Sucesso!"
    else:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Erro ao adicionar tarefa!"
        )

@app.get("/admin/tarefa")
async def get_todas_tarefas():
    return tarefa_database.getTodasTarefas()

if __name__ == "__main__":
    uvicorn.run(app=app)
