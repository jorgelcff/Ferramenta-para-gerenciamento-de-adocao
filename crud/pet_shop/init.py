from pet_shop.operations import venda_produtos, adicionar_produto, listar_produto, atualizar_produto, deletar_produto
print("\n===== PET SHOP - Cesar's Animal Hub =====")

def menu_geral():
    print("\nEscolha uma opção:\n")
    print("1. Vendas")
    print("2. Cadastro de produtos")
    print("3. Voltar para página principal")

def main():
    while True:
        menu_geral()
        op_geral = input("\nQual a opção desejada? ")
        
        if op_geral == '1':
            print("\n>>>> Produtos/Serviços disponíveis para venda <<<<\n")
            listar_produto()
            venda_produtos()
            print("\nVoltando para a página principal...\n")
            break
        
        elif op_geral == '2':
            print("\n1. Adicionar produto")
            print("2. Listar produto")
            print("3. Atualizar produto")
            print("4. Deletar produto")
            print("5. Voltar a página inicial")

            op_cadastro = input("\nQual a opção desejada? ")

            if op_cadastro == '1':
                nome = input("\nDigite o nome do produto: ")
                tipo = input("Digite o tipo do produto: ")
                preco = input("Digite o preço do produto: ")
                adicionar_produto(nome, tipo, preco)
            
            elif op_cadastro == '2':
                listar_produto()
            
            elif op_cadastro == '3':
                id = int(input("\nDigite o ID do produto a ser atualizado: "))
                novo_nome = input("\nDigite o novo nome do produto: ")
                novo_tipo = input("Digite a novo tipo do produto: ")
                novo_preco = input("Digite a novo preço do produto: ")
                atualizar_produto(id, novo_nome, novo_tipo, novo_preco)
            
            elif op_cadastro == '4':
                id = int(input("\nDigite o ID do produto a ser deletado: "))
                deletar_produto(id)

            elif op_cadastro == '5':
                print("\nVoltando ao menu principal...")
                break

            else:
                print("\nOpção inválida! Tente novamente.")
        elif op_geral == 3:
            print("\nVoltando ao menu principal...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            break





