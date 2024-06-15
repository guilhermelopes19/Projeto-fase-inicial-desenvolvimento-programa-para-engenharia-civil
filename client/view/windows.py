import PySimpleGUI as sg
import admin_view
import funcionario_view

def login_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Nome de usuario")], 
        [sg.Input(key="username")],
        [sg.Text("Senha")], 
        [sg.Input(password_char="*",key="password")],
        [sg.Button("Continuar")],
        [sg.Text("Usuario ou Senha Incorretos!", text_color="red",visible=False, key="incorrect_text")]
    ]

    return sg.Window("Login", layout=layout, finalize=True)

def menu_admin_window():
    sg.theme('Reddit')
    layout = [
        [sg.Button("Adicionar Funcionario")],
        [sg.Button("Visualizar Funcionarios")],
        [sg.Button("Criar Tarefa")],
        [sg.Button("Visualizar Tarefas")],
        [sg.Button("Visualizar Relatorios")],
        [sg.Button("Sair")]
    ]

    return sg.Window("Menu Admin", layout=layout, finalize=True)

def menu_func_window():
    sg.theme('Reddit')
    layout = [
        [sg.Button("Visualizar Tarefas")],
        [sg.Button("Adicionar Relatorio")],
        [sg.Button("Visualizar Relatorios")],
        [sg.Button("Sair")]
    ]

    return sg.Window("Menu Funcionario", layout=layout, finalize=True)

def adicionar_func_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Nome do funcionario")],
        [sg.Input(key="nomeFunc")],
        [sg.Text("Senha do funcionario")],
        [sg.Input(key="senhaFunc")],
        [sg.Text("Relatorio cadastrado com sucesso!", text_color="white", background_color="green", visible=False, key="status_true")],
        [sg.Text("Erro ao cadastrar o relatorio! \nTente Novamente!", text_color="white", background_color="red", visible=False, key="status_false")],
        [sg.Button("Cadastrar")],
        [sg.Button("Voltar")]
    ]

    return sg.Window("Adicionar Funcionario", layout=layout, finalize=True)

def adicionar_tarefa_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Nome da Tarefa")],
        [sg.Input(key="nomeTarefa")],
        [sg.Text("Descrição da tarefa")],
        [sg.Input(key="descricao")],
        [sg.Text("Data Prevista de Conclusão (dd-mm-aa)")],
        [sg.Input(key="data_prevista_conclusao")],
        [sg.Text("Selecione os Funcionarios:")]
    ]

    listaFuncionarios = admin_view.visualizarFuncionarios()
    c = 0
    column = []

    if listaFuncionarios == []:
        column.append([sg.Text("Sem funcionarios cadastrados!")])
    else:
        for funcionario in listaFuncionarios:
            column.append([sg.Checkbox(funcionario["nome"],key="{}".format(c))])
            c += 1

    layout.append([sg.Column(column, size=(200, 200), scrollable=True, vertical_scroll_only=True)])

    layout.append([sg.Text("Tarefa cadastrado com sucesso!", text_color="white", background_color="green", visible=False, key="status_true")])
    
    layout.append([sg.Text("Erro ao cadastrar a tarefa! \nTente Novamente!", text_color="white", background_color="red", visible=False, key="status_false")])
    
    layout.append([sg.Button("Cadastrar")])
    
    layout.append([sg.Button("Voltar")])

    return sg.Window("Criar Tarefa", layout=layout, finalize=True), c, listaFuncionarios

def visualizar_funcs_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Funcionarios: ")],
    ]

    listaFuncionarios = admin_view.visualizarFuncionarios()

    if listaFuncionarios == []:
        layout.append([sg.Text("Sem funcionarios cadastrados!")])
    else:
        column = []
        for funcionario in listaFuncionarios:
            column.append([sg.Text("-----------------------------")])
            for key, value in funcionario.items():
                column.append([sg.Text("{}: {}".format(key, value))])
        layout.append([sg.Column(column, size=(500, 500), scrollable=True, vertical_scroll_only=True)])

    layout.append([sg.Button("Voltar")])

    return sg.Window("Visualizar Funcionarios", layout=layout, finalize=True)

def visualizar_tarefas_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Tarefas: ")],
    ]

    listaTarefas = admin_view.visualizarTarefas()

    if listaTarefas == []:
        layout.append([sg.Text("Sem tarefas cadastradas!")])
    else:
        column = []
        for tarefa in listaTarefas:
            column.append([sg.Text("-----------------------------")])
            for key, value in tarefa.items():
                if key == "funcionarios":
                    column.append([sg.Text("Funcionarios:")])
                    for funcionario in value:
                        column.append([sg.Text(funcionario)])
                else:
                    column.append([sg.Text("{}: {}".format(key, value))])
        layout.append([sg.Column(column, size=(500, 500), scrollable=True, vertical_scroll_only=True)])

    layout.append([sg.Button("Voltar")])

    return sg.Window("Visualizar Tarefas", layout=layout, finalize=True)

def visualizar_relatorios_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Relatorios: ")],
    ]

    listaRelatorios = admin_view.visualizarRelatorios()

    if listaRelatorios == []:
        layout.append([sg.Text("Sem relatorios cadastrados!")])
    else:
        column = []
        for relatorio in listaRelatorios:
            column.append([sg.Text("-----------------------------")])
            for key, value in relatorio.items():
                column.append([sg.Text("{}: {}".format(key, value))])
        layout.append([sg.Column(column, size=(500, 500),scrollable=True, vertical_scroll_only=True)])

    layout.append([sg.Button("Voltar")])

    return sg.Window("Visualizar Relatorios", layout=layout, finalize=True)

def visualizar_tarefas_funcionario_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Tarefas: ")],
    ]

    listaTarefas = funcionario_view.visualizarTarefas()

    if listaTarefas == []:
        layout.append([sg.Text("Sem tarefas cadastrados!")])
    else:
        column = []
        for tarefa in listaTarefas:
            column.append([sg.Text("-----------------------------")])
            for key, value in tarefa.items():
                column.append([sg.Text("{}: {}".format(key, value))])
        layout.append([sg.Column(column, size=(500, 500),scrollable=True, vertical_scroll_only=True)])

    layout.append([sg.Button("Voltar")])

    return sg.Window("Visualizar Tarefas", layout=layout, finalize=True)

def adicionar_relatorio_window():
    sg.theme('Reddit')
    layout = [[sg.Text("Selecione a tarefa do relatorio")]]

    listaTarefas = funcionario_view.visualizarTarefas()
    c = 0
    column = []

    if listaTarefas == []:
        column.append([sg.Text("Sem tarefas cadastrados!")])
    else:
        for tarefa in listaTarefas:
            column.append([sg.Radio(tarefa["nome"], group_id=1, key="{}".format(c))])
            c += 1

    layout.append([sg.Column(column, size=(400, 200), scrollable=True, vertical_scroll_only=True)])
    
    layout.append([sg.Text("Texto do relatorio")])
    layout.append([sg.Input(key="texto_relatorio")])

    layout.append([sg.Text("Relatorio cadastrado com sucesso!", text_color="white", background_color="green", visible=False, key="status_true")])
    
    layout.append([sg.Text("Erro ao cadastrar relatorio! \nTente Novamente!", text_color="white", background_color="red", visible=False, key="status_false")])
    
    layout.append([sg.Button("Cadastrar")])
    
    layout.append([sg.Button("Voltar")])

    return sg.Window("Adicionar relatorio", layout=layout, finalize=True), c, listaTarefas

def visualizar_relatorios_funcionario_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Relatorios: ")],
    ]

    listaRelatorios = funcionario_view.visualizarRelatorios()

    if listaRelatorios == []:
        layout.append([sg.Text("Sem relatorios cadastrados!")])
    else:
        column = []
        for relatorio in listaRelatorios:
            column.append([sg.Text("-----------------------------")])
            for key, value in relatorio.items():
                column.append([sg.Text("{}: {}".format(key, value))])
        layout.append([sg.Column(column, size=(500, 500),scrollable=True, vertical_scroll_only=True)])

    layout.append([sg.Button("Voltar")])

    return sg.Window("Visualizar Relatorios", layout=layout, finalize=True)
