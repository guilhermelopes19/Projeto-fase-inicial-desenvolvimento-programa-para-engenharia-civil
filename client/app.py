import requests
import PySimpleGUI as sg
import json
from view import funcionario_view
from view import admin_view
from view import windows

url = "http://127.0.0.1:8000"
 
def main():
    window_login = windows.login_window()
    window_menu_admin = None
    window_menu_func = None
    window_admin_adicionar_func = None
    window_admin_visualizar_func = None
    window_admin_adicionar_tarefa= None
    window_admin_visualizar_tarefas = None
    window_admin_visualizar_relatorios = None
    window_func_visualizar_tarefas = None
    window_func_adicionar_relatorio = None
    window_func_visualizar_relatorios = None

    while True:
        window,event,values = sg.read_all_windows()

        if window == window_login and event == sg.WIN_CLOSED:
            break
        if window == window_login and event== "Continuar":
            
            username = window_login["username"].get()
            password = window_login["password"].get()
            statusLogin= login(username,password)

            if statusLogin.get("status") == True:
                window_login.hide()
                if statusLogin.get("tipo") == "admin":
                    window_menu_admin = windows.menu_admin_window()
                else:
                    window_menu_func = windows.menu_func_window()         
            else:
                window_login["incorrect_text"].update(visible=True)
        if (window==window_menu_admin or window==window_menu_func) and (event==sg.WIN_CLOSED or event=="Sair"):
            window.close()
            window_menu_admin = None
            window_menu_func = None 
            window_login.un_hide()
            window_login["incorrect_text"].update(visible=False)
            window_login["username"].SetFocus()
            window_login["username"].update("")
            window_login["password"].Update("")
        if event == sg.WIN_CLOSED or event== "Voltar":
            if window_menu_admin != None:
                window_menu_admin.un_hide()
            elif window_menu_func != None:
                window_menu_func.un_hide()
            window.close()
            window_admin_adicionar_func = None
            window_admin_visualizar_func = None
            window_admin_adicionar_tarefa= None
            window_admin_visualizar_tarefas = None
            window_admin_visualizar_relatorios = None
            window_func_visualizar_tarefas = None
            window_func_adicionar_relatorio = None
            window_func_visualizar_relatorios = None

        if window == window_menu_admin and event == "Adicionar Funcionario":
            window_menu_admin.hide()
            window_admin_adicionar_func = windows.adicionar_func_window()
        if window == window_menu_admin and event == "Visualizar Funcionario":
            window_menu_admin.hide()
            window_admin_visualizar_func = windows.visualizar_funcs_window()

        if window == window_menu_admin and event == " Criar Tarefa":
            window_menu_admin.hide()
            window_admin_adicionar_tarefa,numFuncionarios,listaFuncionarios = windows.adicionar__window()
        if window == window_menu_admin and event == "Visualizar Tarefas":
            window_menu_admin.hide()
            window_admin_visualizar_tarefas = windows.visualizar_tarefas_window()
        if window == window_menu_admin and event == "Visualizar Relatorios":
            window_menu_admin.hide()
            window_admin_visualizar_relatorios = windows.visualizar_relatorios_window()
        if window == window_menu_func and event == "Visualizar Tarefas":
            window_menu_func.hide()
            window_func_visualizar_tarefas = windows.visualizar_tarefas_funcionario_window()
        if window == window_menu_func and event == "Adicionar Relatorio":
            window_menu_func.hide()
            window_func_adicionar_relatorio,numTarefas, listasTarefas = windows.adicionar_relatorio_window()
        if window == window_menu_func and event == "Visualizar Relatórios":
            window_menu_func.hide()
            window_func_visualizar_relatorios = windows.visualizar_relatorios_window()
        if event == "Cadastrar":
            status=None
            if  window== window_admin_adicionar_func:
                nomeFunc=values["nomeFunc"]
                senhaFunc=values["senhaFunc"]
                status = admin_view.adicionarFuncionario(nomeFunc,senhaFunc)
            elif window == window_admin_adicionar_tarefa:
                nomeTarefa = values["nomeTarefa"]
                descricao = values["descricao"]
                data_prevista_conclusao = values["data_prevista_conclusao"]
                funcionariosId = []
                i = 0
                while i < numFuncionarios:
                    if values[f"{i}"]:
                        funcionariosId.append(listaFuncionarios[i].get("id"))
                    i+=1
                status=admin_view.criarTarefa(nomeTarefa,descricao,data_prevista_conclusao,funcionariosId)
            elif window==window_func_adicionar_relatorio:
                textoRelatorio=values["texto_relatorio"]
                idTarefa=[]
                i=0
                while i<numTarefas:
                    if values[f"{1}"]:
                        idTarefa.append(listasTarefas[i].get("id"))
                    i+=1
                status=funcionario_view.adicionarRelatorio(idTarefa[0],textoRelatorio)
            if status: 
                window["status_true"].update(visible=True)
            else:
                window["status_false"].update(visible=True)
    window_login.close()

def login(username,password):
    
    request = requests.post(url+"/auth", json={"username": username, "password": password})

    if request.status_code == 200:
        # Abre o arquivo user.json para escrita
        file = open("user.json", "w")
        # Escreve os dados da resposta do servidor no arquivo user.json
        json.dump(request.json(), file)
        # Fecha o arquivo
        file.close()
        if request.json()["tipo"] == "admin":
            return {
                "status": True,
                "tipo":"admin"
            }
        elif request.json()["tipo"] == "funcionario":
            return{ 
                "status": True,
                "tipo":"funcionario"
            }
    else:
        return{
            "status": False
        }
    
if __name__ == "__main__":
    main()
