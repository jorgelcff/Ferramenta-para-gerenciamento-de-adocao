import json
import os
import pet_shop.init as pet_shop

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
        maior_id = max(produto["id"] for produto in dados)
        return maior_id + 1

def adicionar_produto(nome, tipo, preco):
    dados = carregar_dados()
    novo_id = gerar_id_unico(dados) 
    novo_produto = {
        "id": novo_id,
        "nome": nome,
        "tipo": tipo,
        "preco": preco
    }
    dados.append(novo_produto)
    salvar_dados(dados)
    print(f"Produto cadastrado com sucesso! ID: {novo_id}")

def listar_produto():
    dados = carregar_dados()
    if not dados: 
        print("Nenhum produto encontrado.")
        return
    for produto in dados:
        print(f"ID: {produto['id']} - Nome: {produto['nome']}, - Tipo: {produto['tipo']}, - Preço: {produto['preco']}")

def atualizar_produto(id, novo_nome, novo_tipo, novo_preco):
    dados = carregar_dados()
    for produto in dados:
        if produto["id"] == id:
            produto["nome"] = novo_nome
            produto["tipo"] = novo_tipo
            produto["preco"] = novo_preco 
            salvar_dados(dados)
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def deletar_produto(id):
    dados = carregar_dados()
    dados = [produto for produto in dados if produto["id"] != id]
    salvar_dados(dados)
    print("Produto removido com sucesso!")

def venda_produtos():
    acumulador_1 = 0
    while True:
        op_produto = input("\nEscolha o produto desejado (ou digite 'sair' para finalizar): ")
        if op_produto.lower() == 'sair':
            print(f"\nO valor final da sua compra é: R$ {acumulador_1:.2f}")
            print("\nAgradecemos a preferência, até a próxima!")
            break
        
        match op_produto:
            case '1': 
                preco_unitario = 50
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '2': 
                preco_unitario = 20
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '3': 
                preco_unitario = 35
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '4': 
                preco_unitario = 15
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '5': 
                preco_unitario = 80
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '6': 
                preco_unitario = 50
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '7': 
                preco_unitario = 100
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '8': 
                preco_unitario = 70
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '9': 
                preco_unitario = 150
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '10':
                preco_unitario = 80
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '11': 
                preco_unitario = 150
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '12':
                preco_unitario = 200
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '13': 
                preco_unitario = 250
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '14': 
                preco_unitario = 500
                quant = int(input("\nQual a quantidade que você deseja? "))
                valor = preco_unitario * quant
            case '15': 
                preco_unitario = 100
                meses = int(input("\nDeseja contratar quantos meses de serviço? "))
                quant = meses
                valor = preco_unitario * quant
        
        acumulador_1 += valor
        print(f"\nProduto adicionado! Valor total acumulado da compra até agora: R$ {acumulador_1:.2f}\n")

