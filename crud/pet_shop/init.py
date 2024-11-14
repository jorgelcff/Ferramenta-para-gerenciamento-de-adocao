from pet_shop.operations import venda_produtos, venda_servicos, venda_pacotes, venda_planos, adicionar_produto, listar_produto, atualizar_produto, deletar_produto
print("===== PET SHOP - Cesar's Animal Hub =====")

def menu_geral():
    print("\nEscolha uma opção:")
    print("1. Vendas")
    print("2. Cadastro de produtos")
    print("3. Voltar para página principal")

def menu_vendas():
    print("1. Produtos")
    print("2. Serviços")
    print("3. Pacotes Especiais")
    print("4. Planos de Saúde")
    print("5. Voltar para página inicial")

def main():
    while True:
        menu_geral()
        op_geral = input("Qual a opção desejada? ")
        
        if op_geral == '1':
            menu_vendas()
            op_vendas = input("Escolha a opção: ")

            if op_vendas == '1':
                print(">>>> Produtos disponíveis <<<<")
                
                listar_produto()

                venda_produtos()

            elif op_vendas == '2':
                print(">>>> Serviços disponíveis <<<<")
                print("1. Banho e tosa - R$ 50,00")
                print("2. Consulta veterinária - R$ 100,00")
                print("3. Vacinação - R$ 70,00")
                print("4. Adestramento - R$ 150,00")
                print("5. Hotel para pets - R$ 80,00/noite")

                venda_servicos()

            elif op_vendas == '3':
                print(">>>> Nossos Pacotes Especiais <<<<")
                print("1. Pacote de Banho Mensal - R$ 150,00")
                print("2. Pacote de Tosa Completa - R$ 200,00")
                print("3. Pacote Saúde Completo (Consulta + Vacinação) - R$ 250,00")
                print("4. Pacote Adestramento - R$ 500,00")

                venda_pacotes()

            elif op_vendas == '4':
                print(">>>> Nossos Planos de Saúde <<<<")
                print("1. Plano Básico - R$ 100,00/mês")
                print("2. Plano Intermediário - R$ 150,00/mês")
                print("3. Plano Avançado - R$ 200,00/mês")
                print("4. Plano Premium - R$ 300,00/mês")

                venda_planos()

            elif op_vendas == '5':
                print("Voltando ao Menu Principal...")
                break  

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        
        elif op_geral == '2':
            print("1. Adicionar produto")
            print("2. Listar produto")
            print("3. Atualizar produto")
            print("4. Deletar produto")
            print("5. Voltar a página inicial")

            op_cadastro = int(input("Qual a opção desejada? "))

            if op_cadastro == '1':
                nome = input("Digite o nome do produto: ")
                tipo = input("Digite o tipo do produto: ")
                preco = input("Digite o preço do produto: ")
                adicionar_produto(nome, tipo, preco)
            
            elif op_cadastro == '2':
                listar_produto()
            
            elif op_cadastro == '3':
                id = int(input("Digite o ID do produto a ser atualizado: "))
                novo_nome = input("Digite o novo nome do produto: ")
                novo_tipo = input("Digite a novo tipo do produto: ")
                novo_preco = input("Digite a novo preço do produto: ")
                atualizar_produto(id, novo_nome, novo_tipo, novo_preco)
            
            elif op_cadastro == '4':
                id = int(input("Digite o ID do produto a ser deletado: "))
                deletar_produto(id)

            elif op_cadastro == '5':
                print("Voltando ao menu principal...")
                break

            else:
                print("Opção inválida! Tente novamente.")




