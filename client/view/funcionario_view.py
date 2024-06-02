import requests
import os
import sys
import json
from datetime import date

url = "http://127.0.0.1:8000"

def menuFunc():
     while True:
        os.system("clear")

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

def visualizarTarefas():
    os.system("clear")

    print("-"*10, " Visualizar Tarefas ", "-"*10)

    file = open("user.json", "r")
    idUser = (json.load(file))["id"]
    file.close()

    request = requests.get(f"{url}/funcionario/tarefas?idUser={idUser}")

    if request.json() == []:
        print("Sem tarefas cadastradas!")
    else:
        for tarefa in request.json():
            print("-"*60)
            for key, value in tarefa.items():
                print(f"{key}: {value}")
            print("-"*60)

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")

def adicionarRelatorio():
    os.system("clear")

    print("-"*10, "Adicionar Relatorios", "-"*10)

    file = open("user.json", "r")
    idUser = (json.load(file))["id"]
    file.close()

    request = requests.get(f"{url}/funcionario/tarefas?idUser={idUser}")

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

    request = requests.put(f"{url}/funcionario/relatorios", json=relatorio)

    if request.status_code == 200:
        print("Relatório adicionado com sucesso!")
    else:
        print("Erro ao adicionar relatório! Tente novamente.")

    input("(PRESSIONE ENTER PARA VOLTAR MENU)")

def visualizarRelatorios():
    os.system("clear")

    print("-"*10, "Visualizar Relatorios", "-"*10)

    file = open("user.json", "r")
    idUser = (json.load(file))["id"]
    file.close()

    request = requests.get(f"{url}/funcionario/relatorios?idUser={idUser}")
    
    if request.json() == []:
        print("Sem relatórios cadastradas!")
    else:
        for relatorio in request.json():
            print("-"*60)
            for key, value in relatorio.items():
                print(f"{key}: {value}")
            print("-"*60)

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")
