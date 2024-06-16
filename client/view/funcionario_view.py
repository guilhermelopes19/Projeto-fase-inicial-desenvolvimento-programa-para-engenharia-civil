import requests
import json
from datetime import date

url = "http://127.0.0.1:8000"   

def visualizarTarefas():

    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.get(f"{url}/funcionario/tarefas?token={token}")
    return request.json()
def adicionarRelatorio(idTarefa, textoRelatorio):
    with open("user.json", "r") as file:
        user_dados = json.load(file)
        idUser = user_dados["id"]
        token = user_dados["token"]

    request = requests.get(f"{url}/funcionario/tarefas?token={token}")

    dataAtual = date.today().strftime("%d-%m-%Y")

    relatorio = {
        "id_user": idUser,
        "id_tarefa": int(idTarefa),
        "texto": textoRelatorio,
        "data_criacao": dataAtual
    }

    request = requests.put(f"{url}/funcionario/relatorios?token={token}", json=relatorio)

    if request.status_code == 200:
        return True
    else:
        return False 
   
def visualizarRelatorios():
    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.get(url+"/funcionario/relatorios?token="+token)
    
    return request.json()