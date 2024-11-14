from pet_shop.operations import venda_produtos, adicionar_produto, listar_produto, atualizar_produto, deletar_produto
from pet_shop.operations import venda_produtos, adicionar_produto, listar_produto, atualizar_produto, deletar_produto
print("===== PET SHOP - Cesar's Animal Hub =====")

def menu_geral():
def menu_geral():
    print("\nEscolha uma opção:")
    print("1. Vendas")
    print("2. Cadastro de produtos")
    print("3. Voltar para página principal")

def main():
    while True:
        menu_geral()
        op_geral = input("Qual a opção desejada? ")
        
        if op_geral == '1':
            print(">>>> Produtos/Serviços disponíveis para venda <<<<")
            listar_produto()
            venda_produtos()
            print("Voltando para a página principal...")
            break
        
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



            else:
                print("Opção inválida! Tente novamente.")




