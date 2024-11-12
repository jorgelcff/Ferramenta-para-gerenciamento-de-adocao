import json
import os
import pet_shop.init as pet_shop
pet_shop.main()

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

acumulador_1 = 0
acumulador_2 = 0
acumulador_3 = 0
acumulador_4 = 0 

def venda_produtos():
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
            if resposta_2.lower() == 's':
                  pet_shop.main()
            else:
                print("Agradecemos a preferência, até a próxima!")

def venda_pacotes():
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
            if resposta_3.lower() == 's':
                  pet_shop.main()
            else:
                print("Agradecemos a preferência, até a próxima!")

def venda_planos():
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
            if resposta_4.lower() == 's':
                pet_shop.main()
            else:
                print("Agradecemos a preferência, até a próxima!")

                