import requests
import os
import sys
import json

url = "http://127.0.0.1:8000"

# Area com as opcoes que o administrador pode executar no sistema
def menuAdmin():
    while True:
        os.system("clear || cls")

        menuOptions = {
            "1": ["Adicionar Funcionário", adicionarFuncionario],
            "2": ["Visualizar Funcionários", visualizarFuncionarios],
            "3": ["Criar Nova Tarefa", criarTarefa],
            "4": ["Visualizar Tarefas", visualizarTarefas],
            "5": ["Visualizar Relatorios", visualizarRelatorios],
            "6": ["Sair", sys.exit]
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

# Area para adicionar um novo funcionario no sistema 
def adicionarFuncionario():
    os.system("clear || cls")

    print("-"*10, " Adicionar Funcionário ", "-"*10)
    
    print("Nome do funcionário: ")
    usernameFunc = input(">> ")
    print("Senha do funcionário: ")
    passwordFunc = input(">> ")

    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.put(url+"/admin/funcionarios?token="+token, json={"username": usernameFunc, "password": passwordFunc})

    if request.status_code == 200:
        print("Funcionario adicionado com sucesso!")
    else:
        print("Erro ao adicionar funcionario! Tente novamente.")

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")

# Area para visualizacao dos funcionarios cadastrados no sistema
def visualizarFuncionarios():
    os.system("clear || cls")

    print("-"*5, " Visualizar Funcionários ", "-"*5)

    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.get(url+"/admin/funcionarios?token="+token)

    if request.json() == []:
        print("Sem funcionarios cadastrados!")
    else:
        for funcionario in request.json():
            print("-"*30)
            for key, value in funcionario.items():
                print(f"{key}: {value}")
            print("-"*30)
    
    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")

# Area para criar uma nova tarefa
def criarTarefa():
    os.system("clear || cls")

    print("-"*10, " Criar Tarefa ", "-"*10)

    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]
    
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

    request = requests.get(url+"/admin/funcionarios?token="+token)

    print("Funcionários")

    for funcionario in request.json():
        print("   id: {}, nome: {}".format(funcionario.get("id"), funcionario.get("nome")))

    print("Digite o id do funcionário (deixe vazio quando concluir): ")

    while True:
        funcionario = input(">> ")

        if funcionario == "":
            break
        else:
            try:
                tarefa.get("funcionariosId").append(int(funcionario))
            except Exception:
                print("Insira um valor válido!")
    
    if tarefa["funcionariosId"] == []:
        print("A tarefa deve ter funcionarios!")
    else:
        request = requests.put(url+"/admin/tarefas?token="+token, json=tarefa)

        if request.status_code == 200:
            print("Tarefa criada com sucesso!")
        else:
            print("Erro ao adicionar tarefa! Tente novamente.")

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")

# Area para visualizar tarefas cadastradas no sistema
def visualizarTarefas():
    os.system("clear || cls")

    print("-"*10, " Visualizar Tarefas ", "-"*10)

    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.get(url+"/admin/tarefas?token="+token)

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

# Area para visualizar relatorios
def visualizarRelatorios():
    os.system("clear || cls")

    print("-"*10, " Visualizar Relatorios ", "-"*10)

    with open("user.json", "r") as file:
        user_dados = json.load(file)
        token = user_dados["token"]

    request = requests.get(url+"/admin/relatorios?token="+token)

    if request.json() == []:
        print("Sem relatórios cadastrados!")
    else:
        for relatorio in request.json():
            print("-"*60)
            for key, value in relatorio.items():
                print(f"{key}: {value}")
            print("-"*60)

    input("(PRESSIONE ENTER PARA VOLTAR AO MENU)")
