from pet_shop.operations import venda_produtos, venda_servicos, venda_pacotes, venda_planos
print("===== PET SHOP - Cesar's Animal Hub =====")

acumulador_1 = 0  # Acumulador para produtos
acumulador_2 = 0  # Acumulador para serviços
acumulador_3 = 0  # Acumulador para pacotes especiais
acumulador_4 = 0  # Acumulador para planos de saúde

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Vendas")
        print("2. Cadastro de produtos/serviços")
        
        op_geral = input("qual a opção desejada? ")
        
        if op_geral == '1':
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

                venda_produtos()

            elif op == '2':
                print(">>>> Serviços disponíveis <<<<")
                print("1. Banho e tosa - R$ 50,00")
                print("2. Consulta veterinária - R$ 100,00")
                print("3. Vacinação - R$ 70,00")
                print("4. Adestramento - R$ 150,00")
                print("5. Hotel para pets - R$ 80,00/noite")

                venda_servicos()

            elif op == '3':
                print(">>>> Nossos Pacotes Especiais <<<<")
                print("1. Pacote de Banho Mensal - R$ 150,00")
                print("2. Pacote de Tosa Completa - R$ 200,00")
                print("3. Pacote Saúde Completo (Consulta + Vacinação) - R$ 250,00")
                print("4. Pacote Adestramento - R$ 500,00")

                venda_pacotes()

            elif op == '4':
                print(">>>> Nossos Planos de Saúde <<<<")
                print("1. Plano Básico - R$ 100,00/mês")
                print("2. Plano Intermediário - R$ 150,00/mês")
                print("3. Plano Avançado - R$ 200,00/mês")
                print("4. Plano Premium - R$ 300,00/mês")

                venda_planos()

            elif op == '5':
                print("Voltando ao Menu Principal...")
                break  

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        
        elif op_geral == '2':
            print("cadastro")

