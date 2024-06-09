import requests
import os
import sys
import json
from datetime import date

url = "http://127.0.0.1:8000"

# Area com as opcoes que o funcionario pode executar no sistema
def menuFunc():
     while True:
        os.system("clear || cls")

        menuOptions = {
            "1": ["Visualizar Tarefas", visualizarTarefas],
            "2": ["Adicionar Relatório", adicionarRelatorio],
            "3": ["Visualizar Relatórios", visualizarRelatorios],
            "4": ["Sair", sys.exit],
        }

        print("-"*10, 'FUNCIONÁRIO', "-"*10)
        for key, value in menuOptions.items():
            print(key, " - ", value[0])
        
        print("Escolha uma das opções:")

        option = input(">> ").strip()

        try:
            (menuOptions[option][1])()
        except Exception:
            pass

# Area para visualizar as tarefas do funcionario cadastradas no sistema
def visualizarTarefas():
    os.system("clear || cls")

    print("-"*10, " Visualizar Tarefas ", "-"*10)

    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.get(f"{url}/funcionario/tarefas?token={token}")

    if request.json() == []:
        print("Sem tarefas cadastradas!")
    else:
        for tarefa in request.json():
            print("-"*60)
            for key, value in tarefa.items():
                print(f"{key}: {value}")
            print("-"*60)

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")

# Area para adicionar um relatorio
def adicionarRelatorio():
    os.system("clear || cls")

    print("-"*10, "Adicionar Relatorios", "-"*10)

    with open("user.json", "r") as file:
        user_dados = json.load(file)
        idUser = user_dados["id"]
        token = user_dados["token"]

    request = requests.get(f"{url}/funcionario/tarefas?token={token}")

    print("Tarefas: ")

    for tarefa in request.json():
        print("   id: {}, nome: {}".format(tarefa.get("id"), tarefa.get("nome")))

    print("Digite o id da tarefa que você deseja fazer o relatório: ")
    idTarefa = int(input(">> "))

    print("Digite o texto do relatório: ")
    textoRelatorio = input(">> ")

    dataAtual = date.today().strftime("%d-%m-%Y")

    relatorio = {
        "id_user": idUser,
        "id_tarefa": idTarefa,
        "texto": textoRelatorio,
        "data_criacao": dataAtual
    }

    request = requests.put(f"{url}/funcionario/relatorios?token={token}", json=relatorio)

    if request.status_code == 200:
        print("Relatório adicionado com sucesso!")
    else:
        print("Erro ao adicionar relatório! Tente novamente.")

    input("(PRESSIONE ENTER PARA VOLTAR MENU)")

# Area para visualizar os relatorios do funcionario
def visualizarRelatorios():
    os.system("clear || cls")

    print("-"*10, "Visualizar Relatorios", "-"*10)

    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.get(f"{url}/funcionario/relatorios?token={token}")
    
    if request.json() == []:
        print("Sem relatórios cadastradas!")
    else:
        for relatorio in request.json():
            print("-"*60)
            for key, value in relatorio.items():
                print(f"{key}: {value}")
            print("-"*60)

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")
