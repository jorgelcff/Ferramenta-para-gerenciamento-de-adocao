from crud.cliente import cadastro

def menu_pet_shop():
    print("===== PET SHOP - Cesar's Animal Hub =====")
    print("1. Produtos")
    print("2. Serviços")
    print("3. Pacotes Especiais")
    print("4. Planos de Saúde")
    print("5. Voltar para página inicial")

def main():
    while True:
        menu_pet_shop()
        op = input("Escolha a opção: ")

        if op == '1':
            print(">>>> Produtos disponíveis <<<<")
            print("1. Ração para cães e gatos - R$ 50,00")
            print("2. Petiscos variados - R$ 20,00")
            print("3. Brinquedos interativos - R$ 35,00")
            print("4. Coleiras e guias - R$ 15,00")
            print("5. Camas e casinhas - R$ 80,00")
            print("6. Shampoos e condicionadores - R$ 25,00")
            print("7. Produtos de higiene - R$ 10,00")
            print("8. Roupas e acessórios - R$ 40,00")
            print("9. Comedouros e bebedouros - R$ 30,00")
            print("10. Suplementos alimentares - R$ 60,00")
            
            op_produto = input("Escolha o produto desejado: ")
            match op_produto:
                case '1':
                    acumulador_1 += 50
                case '2':
                    acumulador_1 += 20
                case '3':
                    acumulador_1 += 35
                case '4':
                    acumulador_1 += 15
                case '5':
                    acumulador_1 += 80
                case '6':
                    acumulador_1 += 25
                case '7':
                    acumulador_1 += 10
                case '8':
                    acumulador_1 += 40
                case '9':
                    acumulador_1 += 30
                case '10':
                    acumulador_1 += 60
            
            print("O valor acumulado dos produtos é: R$", acumulador_1)
            resposta_1 = input("\nDeseja continuar comprando? (S/N) ")
            if resposta_1.lower() == 's':
                continue
            else:
                print("Agradecemos a preferência, até a próxima!")
                break

        elif op == '2':
            print(">>>> Serviços disponíveis <<<<")
            print("1. Banho e tosa - R$ 50,00")
            print("2. Consulta veterinária - R$ 100,00")
            print("3. Vacinação - R$ 70,00")
            print("4. Adestramento - R$ 150,00")
            print("5. Hotel para pets - R$ 80,00/noite")
            
            op_servico = input("Escolha o serviço desejado: ")
            match op_servico:
                case '1':
                    acumulador_2 += 50
                case '2':
                    acumulador_2 += 100
                case '3':
                    acumulador_2 += 70
                case '4':
                    acumulador_2 += 150
                case '5':
                    acumulador_2 += 80
            
            print("O valor acumulado dos serviços é: R$", acumulador_2)
            resposta_2 = input("\nDeseja continuar comprando? (S/N) ")
            if resposta_2.lower() == 's':
                continue
            else:
                print("Agradecemos a preferência, até a próxima!")
                break

        elif op == '3':
            print(">>>> Nossos Pacotes Especiais <<<<")
            print("1. ")
            print("2. ")
            print("3. ")
            print("4. ")
            print("5. ")

        elif op == '4':
            print(">>>> Nossos Planos de Saúde <<<<")
            print("1. ")
            print("2. ")
            print("3. ")
            print("4. ")
            print("5. ")
            op_4 = input("Escolha um plano de saúde adequado para o seu Pet: ")

            if op_4 in ['1', '2', '3', '4']:  
                resposta_4 = input("Você e seu Pet possuem cadastro? (S/N): ")

                if resposta_4.lower() == 'n':  
                    print("Encaminhando para área de cadastro...")
                    cadastro()
                else:
                    id = int(input("Digite o ID do seu animal: "))
                    print("Buscando animal...")

            else:
                print("Voltando ao menu principal...")

        elif op == '5':
            print("Voltando ao Menu Principal...")
            break  

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
