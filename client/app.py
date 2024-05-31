import requests
import os
import json
from view.admin_view import menuAdmin
from view.funcionario_view import menuFunc

url = "http://127.0.0.1:8000"

def login():
    while True:
        os.system("clear")

        print("-"*10, " Login ", "-"*10)

        username = input("Username: ")
        password = input("Password: ")

        request = requests.post(url+"/auth", json={"username": username, "password": password})

        if request.status_code == 200:
            break
        else:
            print("Usuário ou senha incorretos!")
            input("(PRESSIONE ENTER PARA TENTAR NOVAMENTE)")
    
    file = open("user.json", "w")
    json.dump(request.json(), file)
    file.close()

    print("Logado com sucesso!")
    input("(PRESSIONE ENTER PARA CONTINUAR)")

    if request.json()["tipo"] == "admin":
        menuAdmin()
    elif request.json()["tipo"] == "funcionario":
        menuFunc()
    
if __name__ == "__main__":
    login()
