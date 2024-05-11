#Alunos
#Guilherme Souza Lopes - 072320015
#Sara Stephanie Costa - 072320039

# !!! Necessario instalar a biblioteca pandas e openpyxl(utilizada pelo pandas para criar tabelas excel) !!!

import pandas as pd # utilizado para gerenciar os dados e tabelas

# Classe utilizada para gerenciar as tarefas
class TaskManager:
    # funcao construtora da classe que verifica se ja existe uma tabela com dados, se nao cria uma tabela para salvar os dados
    def __init__(self):
        self.pathDB = './database'
        try:
            self.__dfTask = pd.read_excel(f"{self.pathDB}/tasks_table.xlsx")
            print("Lendo dados...")
        except FileNotFoundError:
            print("Criando tabela...")
            self.__dfTask = pd.DataFrame({
                "nomeTarefa": [],
                "equipe": [],
                "equipamentos": [],
                "materiais": [],
            })
            self.updateTable()
    
    # Atualiza a tabela(excel) com os dados presentes na tabela __dfTask(DataFrame do pandas) 
    def updateTable(self):
        self.__dfTask.to_excel(f"{self.pathDB}/tasks_table.xlsx", index=False)
        print("Atualizando tabela...")

    # Adiciona uma nova tarefa a tabela
    def addTask(self, nomeTarefa: str, membrosEquipe: list, equipamentos: list, materiais: list):
        newLine = {
            "nomeTarefa": nomeTarefa,
            "equipe": ', '.join(membrosEquipe),
            "equipamentos": ', '.join(equipamentos),
            "materiais": ', '.join(materiais)
        }
        self.__dfTask = pd.concat([self.__dfTask, pd.DataFrame([newLine])], ignore_index=True)
        self.updateTable()
    
    # Remove uma tarefa da tabela
    def removeTask(self, index):
        try:
            self.__dfTask.drop(index, inplace=True)
            self.__dfTask.reset_index(drop=True, inplace=True)
            self.updateTable()
            print('Removido com sucesso!')
        except KeyError:
            print('Index não encontrado!')

    # Retorna a tabela __dfTask
    def getTableTasks(self):
        return self.__dfTask
