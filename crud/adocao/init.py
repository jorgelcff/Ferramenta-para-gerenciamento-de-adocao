from adocao.operations import adicionar_animal, listar_animais, buscar_animal, atualizar_animal, deletar_animal
def menu_adocao():
    print("===== Gerenciamento de Adoção de Animais =====")
    print("1. Adicionar Animal")
    print("2. Listar Animais")
    print("3. Atualizar Animal")
    print("4. Buscar Animal")
    print("5. Remover Animal")
    print("6. Voltar ao Menu Principal")

def invalido():
    print("Opção invalida tente novamente")
def main():
    while True:
        try:
            menu_adocao()
            op = input("Escolha a opção: ")

            if op == '1':
                nome = input("Digite o nome do animal: ")
                especie = input("Digite a espécie do animal: ")
                raca = input("Digite a raça do animal: ")
                idade = input("Digite a idade do animal: ")
                personalidade = input("Digite a personalidade do animal: ")
                situacao_saude = input("Digite a situação de saúde do animal: ")
                adicionar_animal(nome, especie, raca, idade, personalidade, situacao_saude)

            elif op == '2':
                listar_animais()

            elif op == '3':
                id = int(input("Digite o ID do animal a ser atualizado: "))
                novo_nome = input("Digite o novo nome do animal: ")
                nova_especie = input("Digite a nova espécie do animal: ")
                nova_raca = input("Digite a nova raça do animal: ")
                nova_idade = input("Digite a nova idade do animal: ")
                nova_personalidade = input("Digite a nova personalidade do animal: ")
                nova_situacao_saude = input("Digite a nova situação de saúde do animal: ")
                atualizar_animal(id, novo_nome, nova_especie, nova_raca, nova_idade, nova_personalidade, nova_situacao_saude)

            elif op == '4':
                nome = input("Digite o nome do animal a ser buscado: ")
                buscar_animal(nome=nome)


            elif op == '5':
                id = int(input("Digite o ID do animal a ser deletado: "))
                deletar_animal(id)

            elif op == '6':
                print("Voltando ao menu principal...")
                break

            else:
                print("Opção inválida! Tente novamente.")
        except:
            invalido()