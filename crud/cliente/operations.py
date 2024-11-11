import json
import os

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")

def carregar_dados():
    try:
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def salvar_dados(dados):
    with open(DATA_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4)

def gerar_id_unico(dados):
    if not dados:
        return 1  
    else:
        maior_id = max(cliente["id"] for cliente in dados)
        return maior_id + 1

def adicionar_cliente(nome, cpf, rg, idade, email, cep, telefone):
    dados = carregar_dados()
    novo_id = gerar_id_unico(dados)
    novo_cliente = {
        "id": novo_id,
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "idade": idade,
        "email": email,
        "cep": cep,
        "telefone": telefone
    }
    dados.append(novo_cliente)
    salvar_dados(dados)
    print(f"Cliente adicionado com sucesso! ID: {novo_id}")

def listar_cliente():
    dados = carregar_dados()
    if not dados:
        print("Nenhum cliente encontrado.")
        return
    for cliente in dados:
        print(f"ID: {cliente['id']} - Nome: {cliente['nome']}, CPF: {cliente['cpf']}, RG: {cliente['rg']}, Idade: {cliente['idade']}, E-mail: {cliente['email']}, CEP: {cliente['cep']}, Telefone: {cliente['telefone']}")

def atualizar_cliente(cpf, novo_nome, novo_rg, nova_idade, novo_email, novo_cep, novo_telefone):
    dados = carregar_dados()
    for cliente in dados:
        if cliente["cpf"] == cpf:
            cliente["nome"] = novo_nome
            cliente["rg"] = novo_rg
            cliente["idade"] = nova_idade
            cliente["email"] = novo_email
            cliente["cep"] = novo_cep
            cliente["telefone"] = novo_telefone
            salvar_dados(dados)
            print("Cliente atualizado com sucesso!")
            return
    print("Cliente não encontrado.")

def buscar_cliente(cpf):
    dados = carregar_dados()
    for cliente in dados:
        if cliente["cpf"] == cpf:
            print(f"ID: {cliente['id']} - Nome: {cliente['nome']}, CPF: {cliente['cpf']}, RG: {cliente['rg']}, Idade: {cliente['idade']}, E-mail: {cliente['email']}, CEP: {cliente['cep']}, Telefone: {cliente['telefone']}")
            return
    print("Cliente não encontrado.")

def remover_cliente(cpf):
    dados = carregar_dados()
    dados = [cliente for cliente in dados if cliente["cpf"] != cpf]
    salvar_dados(dados)
    print("Cliente removido com sucesso!")