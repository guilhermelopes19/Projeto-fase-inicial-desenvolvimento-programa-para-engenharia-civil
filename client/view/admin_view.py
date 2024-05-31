import requests
import os
import sys

url = "http://127.0.0.1:8000"

def menuAdmin():
    while True:
        os.system("clear")

        menuOptions = {
            "1": ["Adicionar Funcionário", adicionarFuncionario],
            "2": ["Visualizar Funcionários", visualizarFuncionarios],
            "3": ["Criar Nova Tarefa", criarTarefa],
            "4": ["Visualizar Tarefas", visualizarTarefas],
            "5": ["Visualizar Relatorios", visualizarRelatorios],
            "6": ["Sair", sys.exit],
        }

        print("-"*10, 'ADMIN', "-"*10)
        for key, value in menuOptions.items():
            print(key, " - ", value[0])
        
        print("Escolha uma das opções:")

        option = input(">> ").strip()

        try:
            (menuOptions[option][1])()
        except Exception:
            pass

def adicionarFuncionario():
    os.system("clear")

    print("-"*10, " Adicionar Funcionário ", "-"*10)
    
    print("Nome do funcionário: ")
    usernameFunc = input(">> ")
    print("Senha do funcionário: ")
    passwordFunc = input(">> ")

    request = requests.put(url+"/admin/funcionarios", json={"username": usernameFunc, "password": passwordFunc})

    if request.status_code == 200:
        print("Funcionario adicionado com sucesso!")
    else:
        print("Erro ao adicionar funcionario! Tente novamente.")

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")

def visualizarFuncionarios():
    os.system("clear")

    print("-"*5, " Visualizar Funcionários ", "-"*5)

    request = requests.get(url+"/admin/funcionarios")

    if request.json() == []:
        print("Sem funcionarios cadastrados!")
    else:
        for funcionario in request.json():
            print("-"*30)
            for key, value in funcionario.items():
                print(f"{key}: {value}")
            print("-"*30)
    
    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")

def criarTarefa():
    os.system("clear")

    print("-"*10, " Criar Tarefa ", "-"*10)
    tarefa = {
        "nome": "",
        "descricao": "",
        "data_prevista_conclusao": "",
        "funcionariosId": []
    }

    print("Digite o nome da tarefa: ")
    tarefa["nome"] = input(">> ")

    print("Digite a descricao da tarefa: ")
    tarefa["descricao"] = input(">> ")

    print("Digite a data prevista para conclusão(formato dd-mm-aaaa): ")
    tarefa["data_prevista_conclusao"] = input(">> ")

    request = requests.get(url+"/admin/funcionarios")

    print("Funcionários")

    for funcionario in request.json():
        print("   id: {}, nome: {}".format(funcionario.get("id"), funcionario.get("nome")))

    print("Digite o id do funcionário (deixe vazio quando concluir): ")

    while True:
        funcionario = input(">> ")

        if funcionario is "":
            break
        else:
            try:
                tarefa.get("funcionariosId").append(int(funcionario))
            except Exception:
                print("Insira um valor válido!")
    
    if tarefa["funcionariosId"] == []:
        print("A tarefa deve ter funcionarios!")
    else:
        request = requests.put(url+"/admin/tarefas", json=tarefa)

        if request.status_code == 200:
            print("Tarefa criada com sucesso!")
        else:
            print("Erro ao adicionar tarefa! Tente novamente.")

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")

def visualizarTarefas():
    os.system("clear")

    print("-"*10, " Visualizar Tarefas ", "-"*10)

    request = requests.get(url+"/admin/tarefas")

    if request.json() == []:
        print("Sem tarefas cadastradas!")
    else:
        for tarefa in request.json():
            print("-"*60)
            for key, value in tarefa.items():
                if key == "funcionarios":
                    print(f"{key}: ")
                    for nomeFunc in value:
                        print(f"   {nomeFunc}")
                else:
                    print(f"{key}: {value}")
            print("-"*60)

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")

def visualizarRelatorios():
    os.system("clear")

    print("-"*10, " Visualizar Relatorios ", "-"*10)

    request = requests.get(url+"/admin/relatorios")

    if request.json() == []:
        print("Sem relatórios cadastradas!")
    else:
        for relatorio in request.json():
            print("-"*60)
            for key, value in relatorio.items():
                print(f"{key}: {value}")
            print("-"*60)

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")
