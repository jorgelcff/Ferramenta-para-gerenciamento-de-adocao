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
        "preço": preco
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
            produto["preço"] = novo_preco 
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
            op_produto = input("Escolha o produto desejado: ")
            match op_produto:
                case '1': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 50 * quant
                case '2': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 20 * quant
                case '3': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 35 * quant
                case '4': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 15 * quant
                case '5': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 80 * quant
            acumulador_1 = acumulador_1 + valor
            print("O valor acumulado dos produtos é: R$", acumulador_1)
            resposta_1 = input("\nDeseja continuar comprando? (S/N) ")
            if resposta_1.lower() == 's':
                pet_shop.main()
            else:
                print("Agradecemos a preferência, até a próxima!")

def venda_servicos():
        acumulador_2 = 0
        while True: 
            op_servico = input("Escolha o serviço desejado: ")
            match op_servico:
                case '1': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 50 * quant
                case '2': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 100 * quant
                case '3': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 70 * quant
                case '4': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 150 * quant
                case '5':
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 80 * quant
            acumulador_2 = acumulador_2 + valor
            print("O valor acumulado dos serviços é: R$", acumulador_2)
            resposta_2 = input("\nDeseja continuar comprando? (S/N) ")
            if resposta_2.lower() == 'S':
                pet_shop.main()
                break
            elif resposta_2.lower() == 'N':
                print("Agradecemos a preferência, até a próxima!")
                break

def venda_pacotes():
        acumulador_3 = 0
        while True:
            op_pacote = input("Escolha o pacote desejado: ")
            match op_pacote:
                case '1': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 150 * quant
                case '2':
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 200 * quant
                case '3': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 250 * quant
                case '4': 
                        quant = int(input("Qual a quantidade que você deseja? "))
                        valor = 500 * quant
            acumulador_3 = acumulador_3 + valor
            print("O valor acumulado dos pacotes especiais é: R$", acumulador_3)
            resposta_3 = input("\nDeseja continuar comprando? (S/N) ")
            if resposta_3.lower() == 'S':
                  pet_shop.main()
            else:
                print("Agradecemos a preferência, até a próxima!")

def venda_planos():
            acumulador_4 = 0
            op_plano = input("Escolha um plano de saúde adequado para o seu Pet: ")
            match op_plano:
                case '1': 
                        meses = int(input("Deseja contratar quantos meses de serviço? "))
                        valor = 100 * meses
                case '2': 
                        meses = int(input("Deseja contratar quantos meses de serviço? "))
                        valor = 150 * meses
                case '3': 
                        meses = int(input("Deseja contratar quantos meses de serviço? "))
                        valor = 200 * meses
                case '4': 
                        meses = int(input("Deseja contratar quantos meses de serviço? "))
                        valor = 300 * meses
            acumulador_4 = acumulador_4 + valor
            print("O valor acumulado dos planos de saúde é: R$", acumulador_4)
            resposta_4 = input("\nDeseja continuar comprando? (S/N) ")
            if resposta_4.lower() == 'S':
                pet_shop.main()
            else:
                print("Agradecemos a preferência, até a próxima!")