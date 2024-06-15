# Projeto Gerenciador de Tarefas 🗒️

Pensando no futuro, onde se deseja um ambiente produtivo e organizado, teve-se como ideia, a criação de um programa em python que fosse capaz gerenciar tarefas básicas de uma obra da construção civil, buscando proporcionar uma maior organização nas tarefas que deverão ser executadas.

## Requisitos

> [!NOTE]
> O projeto foi desenvolvido com python 3.11

### Servidor 🖥
As bibliotecas necessarias para o servidor podem ser instaladas com o seguinte comando: 
```bash
#Estando na pasta raiz do projeto
cd server
pip install -r requirements.txt
``` 

As seguintes bibliotecas serão instaladas

- FastAPI
- Uvicorn
- Pydantic

### Cliente 💻
As bibliotecas necessarias para o cliente podem ser instaladas com o seguinte comando: 
```bash
#Estando na pasta raiz do projeto
cd client
pip install -r requirements.txt
```
A seguinte biblioteca sera instalada
- Requests

## Como rodar ⚙️

Para o funcionamento do programa, o servidor deve estar rodando. Siga os passos abaixo:

1. **Rodando o servidor**:

Execute o arquivo ```main.py``` do servidor:
```bash
#Estando na pasta raiz do projeto
cd server
python main.py
```

> [!WARNING]
> O uvicorn configura o servidor no endereco http://127.0.0.1/8000. Certifique-se que esta porta esta livre.

2. **Rodando o cliente**:

Após iniciar o servidor, deixe em segundo plano, abra um novo terminal e execute o arquivo ```app.py``` do cliente:
```bash
#Estando na pasta raiz do projeto
cd client
python app.py
```

## Contribuidores 
- Guilherme Lopes [(Github)](https://github.com/guilhermelopes19)
- Sara Stephanie [(Github)](https://github.com/sarastephanie)
