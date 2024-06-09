import requests
import os
import json
from view.admin_view import menuAdmin
from view.funcionario_view import menuFunc

url = "http://127.0.0.1:8000"

# Area para o usuario inserir nome de usuario e senha. Envia para servidor que valida o usuario, pode seguir para o menu do administrador, para o menu do funcionario ou caso o usuario nao seja encontrado permitir que o usuario digite o nome de usuario e senha novamente 
def login():
    while True:
        os.system("clear || cls")

        print("-"*10, " Login ", "-"*10)

        username = input("Username: ")
        password = input("Password: ")

        request = requests.post(url+"/auth", json={"username": username, "password": password})

        if request.status_code == 200:
            break
        else:
            print("Usuário ou senha incorretos!")
            input("(PRESSIONE ENTER PARA TENTAR NOVAMENTE)")
    # Abre o arquivo user.json para escrita
    file = open("user.json", "w")
    # Escreve os dados da resposta do servidor no arquivo user.json
    json.dump(request.json(), file)
    # Fecha o arquivo
    file.close()

    print("Logado com sucesso!")
    input("(PRESSIONE ENTER PARA CONTINUAR)")

    if request.json()["tipo"] == "admin":
        menuAdmin()
    elif request.json()["tipo"] == "funcionario":
        menuFunc()
    
if __name__ == "__main__":
    login()
