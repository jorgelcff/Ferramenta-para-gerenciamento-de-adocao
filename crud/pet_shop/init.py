from crud.cliente import cadastro

def menu_pet_shop():
    print("===== PET SHOP - Cesar's Animal Hub =====")
    print("1. Produtos")
    print("2. Serviços")
    print("3. Pacotes Especiais")
    print("4. Planos de Saúde")
    print("5. Voltar ao Menu Principal")

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

        elif op == '2':
            print(">>>> Serviços disponíveis <<<<")
            print("1. Banho e tosa - R$ 50,00")
            print("2. Consulta veterinária - R$ 100,00")
            print("3. Vacinação - R$ 70,00")
            print("4. Adestramento - R$ 150,00")
            print("5. Hotel para pets - R$ 80,00/noite")

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
