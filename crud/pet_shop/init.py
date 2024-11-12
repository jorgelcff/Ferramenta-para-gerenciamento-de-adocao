print("===== PET SHOP - Cesar's Animal Hub =====")

acumulador_1 = 0  # Acumulador para produtos
acumulador_2 = 0  # Acumulador para serviços
acumulador_3 = 0  # Acumulador para pacotes especiais
acumulador_4 = 0  # Acumulador para planos de saúde

while True:
    print("\nEscolha uma opção:")
    print("1. Produtos")
    print("2. Serviços")
    print("3. Pacotes Especiais")
    print("4. Planos de Saúde")
    print("5. Voltar para página inicial")

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
            case '1': acumulador_1 += 50
            case '2': acumulador_1 += 20
            case '3': acumulador_1 += 35
            case '4': acumulador_1 += 15
            case '5': acumulador_1 += 80
            case '6': acumulador_1 += 25
            case '7': acumulador_1 += 10
            case '8': acumulador_1 += 40
            case '9': acumulador_1 += 30
            case '10': acumulador_1 += 60

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
            case '1': acumulador_2 += 50
            case '2': acumulador_2 += 100
            case '3': acumulador_2 += 70
            case '4': acumulador_2 += 150
            case '5': acumulador_2 += 80

        print("O valor acumulado dos serviços é: R$", acumulador_2)
        resposta_2 = input("\nDeseja continuar comprando? (S/N) ")
        if resposta_2.lower() == 's':
            continue
        else:
            print("Agradecemos a preferência, até a próxima!")
            break

    elif op == '3':
        print(">>>> Nossos Pacotes Especiais <<<<")
        print("1. Pacote de Banho Mensal - R$ 150,00")
        print("2. Pacote de Tosa Completa - R$ 200,00")
        print("3. Pacote Saúde Completo (Consulta + Vacinação) - R$ 250,00")
        print("4. Pacote Adestramento - R$ 500,00")

        op_pacote = input("Escolha o pacote desejado: ")
        match op_pacote:
            case '1': acumulador_3 += 150
            case '2': acumulador_3 += 200
            case '3': acumulador_3 += 250
            case '4': acumulador_3 += 500

        print("O valor acumulado dos pacotes especiais é: R$", acumulador_3)
        resposta_3 = input("\nDeseja continuar comprando? (S/N) ")
        if resposta_3.lower() == 's':
            continue
        else:
            print("Agradecemos a preferência, até a próxima!")
            break

    elif op == '4':
        print(">>>> Nossos Planos de Saúde <<<<")
        print("1. Plano Básico - R$ 100,00/mês")
        print("2. Plano Intermediário - R$ 150,00/mês")
        print("3. Plano Avançado - R$ 200,00/mês")
        print("4. Plano Premium - R$ 300,00/mês")

        op_plano = input("Escolha um plano de saúde adequado para o seu Pet: ")
        match op_plano:
            case '1': acumulador_4 += 100
            case '2': acumulador_4 += 150
            case '3': acumulador_4 += 200
            case '4': acumulador_4 += 300

        print("O valor acumulado dos planos de saúde é: R$", acumulador_4)
        resposta_4 = input("\nDeseja continuar comprando? (S/N) ")
        if resposta_4.lower() == 's':
            continue
        else:
            print("Agradecemos a preferência, até a próxima!")
            break

    elif op == '5':
        print("Voltando ao Menu Principal...")
        break  

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

