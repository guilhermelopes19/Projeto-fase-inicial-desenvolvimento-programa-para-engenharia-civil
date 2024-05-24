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

if __name__ == "__main__":
    uvicorn.run(app=app)
