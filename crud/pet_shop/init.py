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
            print("1. ")
            print("2. ")
            print("3. ")
            print("4. ")
            print("5. ")
            print("6. ")
            print("7. ")
            print("8. ")
            print("9. ")
            print("10. ")

        elif op == '2':
            print(">>>> Serviços disponíveis <<<<")
            print("1. ")
            print("2. ")
            print("3. ")
            print("4. ")
            print("5. ")

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
            op_4 = input("Escolha um plano de saúde adequando com o seu Pet")

                if op_4 == 1 or op_4 == 2 or op_4 == 3 or op_4 == 4:
                    resposta_4 = input("Você e seu Pet possuem cadastro? (S/N)")
                        if resposta_4 == 'N' or resposta_4 == "n":
                            print("Encaminhando para área de cadastro...")
                            cadastro()
                        else:
                            id = int(input("Digite o ID do seu animal: "))
                            print("Buscando animal...")
                else:
                    print("Voltando ao menu principal...")


            