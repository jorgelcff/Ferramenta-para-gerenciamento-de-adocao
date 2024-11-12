from pet_shop.operations import acumulador_geral, acumulador_3, acumulador_4

def menu_pet_shop():
    print("===== PET SHOP - Cesar's Animal Hub =====")
    print("1. Produtos")
    print("2. Serviços")
    print("3. Pacotes Especiais")
    print("4. Planos de Saúde")
    print("5. Voltar para página inicial")

def main():
    global acumulador_geral, acumulador_3, acumulador_4
    acumulador_geral = 0
    acumulador_1 = 0
    acumulador_2 = 0
    acumulador_3 = 0
    acumulador_4 = 0
    
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
            print("1. Banho e tosa + shampoo e condicionador ---------------> R$ 70")
            print("2. Banho e tosa + consulta veterinária + vacinação ------> R$ 200")
            print("3. Hotel pets (noite) + banho e tosa + alimentação ------> R$ 180")
            print("4. Adestramento (2x sessão) + hotel pets (2x semana) ----> R$ 350")
            print("5. Voltar ao menu principal\n")
            print("É permitida a compra conjunta de pacotes para diferentes animais!\n")
            
            op_3 = input("Escolha o pacote que mais se encaixa na necessidade do seu(s) pet(s): \n")
            match op_3:
                case '1': 
                    pets = int(input("Quantos pets vão utilizar o serviço? "))
                    valor = 70 * pets
                case '2':
                    pets = int(input("Quantos pets vão utilizar o serviço? "))
                    valor = 200 * pets
                case '3':
                    pets = int(input("Quantos pets vão utilizar o serviço? "))
                    valor = 180 * pets
                case '4':
                    pets = int(input("Quantos pets vão utilizar o serviço? "))
                    valor = 350 * pets
                case '5': 
                    continue
            
            acumulador_3 += valor
            print("O valor da compra de seus Pacotes Especiais é: ", acumulador_3)
            resposta_3 = input("\nDeseja continuar comprando? (S/N) ")
            if resposta_3.lower() == 's':
                continue
            else:
                print("Agradecemos a preferência, até a próxima!")
                break

        elif op == '4':
            print(">>>> Nossos Planos de Saúde <<<<")
            print("1. Plano Básico -----------> R$ 50")
            print("2. Plano Básico Plus ------> R$ 70")
            print("3. Plano Intermediário ----> R$ 90")
            print("4. Plano Premium ----------> R$ 120")
            print("5. Voltar ao menu principal")
            
            op_4 = input("Escolha um plano de saúde adequado para o seu Pet: ")
            match op_4:
                case '1': 
                    meses = int(input("Por quantos meses deseja contratar? "))
                    valor = 50 * meses
                case '2':
                    meses = int(input("Por quantos meses deseja contratar? "))
                    valor = 70 * meses
                case '3':
                    meses = int(input("Por quantos meses deseja contratar? "))
                    valor = 90 * meses
                case '4':
                    meses = int(input("Por quantos meses deseja contratar? "))
                    valor = 120 * meses
                case '5': 
                    continue
            
            acumulador_4 += valor
            print("O valor do seu Plano de Saúde é: ", acumulador_4)
            resposta_4 = input("\nDeseja continuar comprando? (S/N) ")
            if resposta_4.lower() == 's':
                continue
            else:
                print("Agradecemos a preferência, até a próxima!")
                break
        
        elif op == '5':
            print("Voltando para página inicial...")
            break

    acumulador_geral = acumulador_1 + acumulador_2 + acumulador_3 + acumulador_4
    print("O valor total de suas compras em nosso Pet Shop foi: R$ ", acumulador_geral)
