import requests
import json

url = "http://127.0.0.1:8000"

def adicionarFuncionario(usernameFunc,passwordFunc):
    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.put(url+"/admin/funcionarios?token="+token, json={"username": usernameFunc, "password": passwordFunc})

    if request.status_code == 200:
       return True
    else:
       return False


def visualizarFuncionarios():

    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.get(url+"/admin/funcionarios?token="+token)
    return request.json() 

def criarTarefa(nome,descricao,data_prevista_conclusao,funcionariosId):
   
    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]
    
    tarefa = {
        "nome":nome,
        "descricao": descricao,
        "data_prevista_conclusao": data_prevista_conclusao,
        "funcionariosId": funcionariosId
    }
    request = requests.put(url+"/admin/tarefas?token="+token, json=tarefa)

    if request.status_code == 200:
        return True
    else:
        return False

def visualizarTarefas():
    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.get(url+"/admin/tarefas?token="+token)

    return request.json()
def visualizarRelatorios():
    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.get(url+"/admin/relatorios?token="+token)

    return request.json()
 