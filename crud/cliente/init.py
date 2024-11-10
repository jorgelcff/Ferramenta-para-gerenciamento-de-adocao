from cliente.operations import adicionar_cliente, listar_cliente, atualizar_cliente, buscar_cliente, remover_cliente;
def menu_cliente():
    print("===== Cadastro Clientes =====")
    print("1. Adicionar Cliente")
    print("2. Listar Clientes")
    print("3. Atualizar Cliente")
    print("4. Buscar Cliente")
    print("5. Remover Cliente")
    print("6. Voltar ao Menu Principal")

    def main():
    while True:
        menu_cliente()
        op = input("Escolha uma opção: ")

        if op == '1':
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o cpf do cliente: ")
            rg = input("Digite o rg do cliente: ")
            idade = input("Digite a idade do cliente: ")
            email = input("Digite o E-mail do cliente: ")
            cep = input("Digite o cep do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            adicionar_cliente(nome, cpf, rg, idade, email, cep, telefone)

        elif op == '2':
            listar_cliente()

        elif op == '3':
            cpf = input("Digite o cpf do cliente a ser atualizado: ")
            novo_nome = input("Digite o novo nome do cliente: ")
            novo_rg = input("Digite a novo rg do cliente: ")
            nova_idade = input("Digite a nova idade do cliente: ")
            novo_email = input("Digite o novo email do cliente: ")
            novo_cep = input("Digite o novo cep do cliente: ")
            novo_telefone = input("Digite o novo telefone do cliente: ")
            atualizar_cliente(novo_nome, novo_rg, nova_idade, novo_email, novo_cep, novo_telefone)

        elif op == '4':
            id = input("Digite o cpf do cliente a ser buscado: ")
            buscar_cliente(cpf)

        elif op == '5':
            cpf = input("Digite o cpf do cliente a ser deletado: ")
            remover_cliente(cpf)
        
        elif op == '6':
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida! Tente novamente.")