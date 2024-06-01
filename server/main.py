from fastapi import FastAPI, HTTPException, status
import uvicorn
from contextlib import asynccontextmanager 
from src import database, user_database, tarefa_database, relatorio_database
from src.models.user_model import UserIn
from src.models.tarefa_model import Tarefa
from src.models.relatorio_model import Relatorio

app = FastAPI()

# inicializa o banco de dados de forma assincrona 
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.inicializarBancoDados()
    yield

# Executa a funcao lifespan junto com a inicializacao do servidor
app.router.lifespan_context = lifespan

# Rota de autenticao. Recebe usuario e senha do client e valida se usuario está cadastrado no banco de dados
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

# Rota para adicionar funcionario, recebe nome de usuario e senha
@app.put("/admin/funcionarios")
async def adicionar_funcionario(func: UserIn):
    if user_database.adicionarFuncionario(func=func):
        return "Funcionario Adicionado com Sucesso!"
    else:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Erro ao adicionar novo funcionario!"
        )

# Rota que lista todos os funcionario cadastrados no banco de dados
@app.get("/admin/funcionarios")
async def lista_funcionarios():
    return user_database.getFuncionarios()

# Rota que adiciona uma nova tarefa do banco de dados. Recebe nome, descricao, data prevista de conclusao e id dos funcionarios
@app.put("/admin/tarefas")
async def adicionar_tarefa(tarefa: Tarefa):
    if tarefa_database.adicionarTarefa(tarefa=tarefa):
        return "Tarefa adicionada com Sucesso!"
    else:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Erro ao adicionar tarefa!"
        )

# Rota que lista todas as tarefas cadastradas no sistema
@app.get("/admin/tarefas")
async def get_todas_tarefas():
    return tarefa_database.getTodasTarefas()

# Rota que lista todos os relatorios cadastrados no sistema
@app.get("/admin/relatorios")
async def get_todos_relatorios():
    return relatorio_database.getTodosRelatorios()

# Rota que lista todas as tarefas do funcionario. Recebe o id do usuário
@app.get("/funcionario/tarefas")
async def get_funcionario_tarefas(idUser: int):
    return tarefa_database.getTarefasFuncionario(idUser=idUser)

# Rota que adiciona um novo relatorio. Recebe id do usuario, id da tarefa, texto, data de criacao
@app.put("/funcionario/relatorios")
async def adicionar_relatorio(relatorio: Relatorio):
    if relatorio_database.adicionarRelatorio(relatorio=relatorio):
        return "Relatorio adicionado com sucesso!"
    else:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Erro ao adicionar tarefa!"
        )

# Rota que lista todos relatorios cadastrados pelo funcionario
@app.get("/funcionario/relatorios")
async def relatorios_cadastrados(idUser: int):
    return relatorio_database.getRelatoriosFuncionario(idUser=idUser)

# Inicializa o servidor se o arquivo for o principal
if __name__ == "__main__":
    uvicorn.run(app=app)
