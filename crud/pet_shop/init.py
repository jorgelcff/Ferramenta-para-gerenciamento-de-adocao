from pet_shop.operations import acumulador_geral, acumulador_3, acumulador_4
def menu_pet_shop():
    print("===== PET SHOP - Cesar's Animal Hub =====")
    print("1. Produtos")
    print("2. Serviços")
    print("3. Pacotes Especiais")
    print("4. Planos de Saúde")
    print("5. Voltar para página inicial")

def main():
    acumulador_geral
    acumulador_3
    acumulador_4
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
            print("1. Banho e tosa + shampoo e condicionador ---------------> R$ 70")
            print("2. Banho e tosa + consulta veterinária + vacinação ------> R$ 200")
            print("3. Hotel pets (noite) + banho e tosa + alimentação ------> R$ 180")
            print("4. Adestramento (2x sessão) + hotel pets (2x semana) ----> R$ 350")
            print("5. Voltar ao menu principal\n")
            print("É permitida a comprar conjunta de pacotes para diferentes animais!\n")
            op_3 = input("Escolha o pacote que mais se encaixa na necessidade do seu(s) pet(s): \n")
            match op_3:
                case 1: 
                    pets = int(input("Quantos pets vão utilizar o serviço? "))
                    valor = 70 * pets
                case 2:
                    pets = int(input("Quantos pets vão utilizar o serviço? "))
                    valor = 200 * pets
                case 3:
                   pets = int(input("Quantos pets vão utilizar o serviço? "))
                   valor = 180 * pets
                case 4:
                    pets = int(input("Quantos pets vão utilizar o serviço? "))
                    valor = 350 * pets
                case 5: 
                    main()
                    continue
            acumulador_3 = acumulador_3 + valor
            print("O valor da compra de seus Pacotes Especiais é: ", acumulador_3)
            resposta_3 = input("\nDeseja continuar comprando? (S/N)")
            if resposta_3 == 'S' or resposta_3 == 's':
                main()
                continue
            else:
                print("Agradeçemos a preferência, até a próxima!")
                break


        elif op == '4':
            print(">>>> Nossos Planos de Saúde <<<<")
            print("1. Plano Básico -----------> R$ 50")
            print("2. Plano Básico Plus ------> R$ 70")
            print("3. Plano Intermediário ----> R$ 90")
            print("4. Plano Premium ----------> R$ 120")
            print("5. Voltar ao menu principal")
            op_4 = input("Escolha um plano de saúde adequando com o seu Pet: ")
            match op_4:
                case 1: 
                    meses = int(input("Por quantos meses deseja contratar? "))
                    valor = 50 * meses
                case 2:
                    meses = int(input("Por quantos meses deseja contratar? "))
                    valor = 70 * meses
                case 3:
                    meses = int(input("Por quantos meses deseja contratar? "))
                    valor = 90 * meses
                case 4:
                    meses = int(input("Por quantos meses deseja contratar? "))
                    valor = 120 * meses
                case 5: 
                    main()
                    continue
            acumulador_4 = acumulador_4 + valor
            print("O valor do seu Plano de Saúde é: ", acumulador_4)
            resposta_4 = input("\nDeseja continuar comprando? (S/N)")
            if resposta_4 == 'S' or resposta_3 == 's':
                main()
                continue
            else:
                print("Agradeçemos a preferência, até a próxima!")
                break
        
        else:
            print("Voltando para página inicial...")

    acumulador_geral = acumulador_geral + acumulador_3 + acumulador_4
    print("O valor total de suas compras em nosso Pet shop foi: R$ ", acumulador_geral)


        


            