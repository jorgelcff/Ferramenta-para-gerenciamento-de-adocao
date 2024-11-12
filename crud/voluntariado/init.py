from voluntariado.operations import adicionar_voluntario, adicionar_voluntario_veterinario, listar_voluntario, listar_veterinario, deletar_veterinario, deletar_voluntario, atualizar_voluntario, atualizar_veterinario
import os 

def menu_voluntariado():
    print("===== Venha fazer parte do nosso time!! =====")
    print("1. Cadastro para voluntário geral")
    print("2. Cadastro para voluntário médico")
    print("3. Listar voluntário geral e seus dias")
    print("4. Listar voluntário médico e seus dias")
    print("5. Atualizar voluntário geral")
    print("6. Atualizar voluntário médico")
    print("7. buscar voluntário geral")
    print("8. buscar voluntário médico")
    print("9. Remover voluntário geral")
    print("10. Remover voluntário médico")
    print("11. Voltar ao Menu Principal")

def main():
    while True:
        menu_voluntariado()
        op = input("Escolha uma das opções: ")
        if op == '1':
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade "))
            if idade <18:
                print("Infelizmente não estamos aceitando voluntários menores de idade no momento, agradecemos por querer ajudar!! 🥰 ")
                break
            contato = input("Digite seu email para contato:")
            mes = input("Digite a quantidade de vezes que podera comparecer para ser voluntario no mês")
            adicionar_voluntario(nome, idade, contato, mes)
            
        elif op =='2':
            nome = input("Digite seu nome: ")
            contato = input("Digite seu email para contato:")
            especialidade = input("Digite sua expecialidade:")
            dia = input("Digite o dia que podera atender:")
            adicionar_voluntario_veterinario(nome, contato, especialidade, dia)
        elif op == '3':
            listar_voluntario()
        elif op == '4':
            listar_veterinario()
        elif op =='5':
            id = int(input("Digite o ID do voluntário a ser atualizado: "))
            novo_nome = input("Digite o novo nome do voluntário: ")
            nova_idade = input("Digite a nova idade do voluntário: ")
            novo_contato = input("Digite a nova personalidade do voluntário: ")
            novo_mes = input("Digite a nova situação de saúde do voluntário: ")
            atualizar_voluntario(id, novo_nome, nova_idade, novo_contato, novo_mes)

        elif op =='6':
            id = int(input("Digite o ID do veterinário a ser atualizado: "))
            novo_nome = input("Digite o novo nome do veterinário: ")
            nova_idade = input("Digite a nova idade do veterinário: ")
            novo_contato = input("Digite o contato do veterinário: ")
            novo_mes = input("Digite a nova situação de saúde do veterinário: ")
            atualizar_veterinario(id, novo_nome, nova_idade, novo_contato, novo_mes)
             
        elif op =='7':
            
        elif op =='8':
            
        elif op == '9':
                id = int(input("Digite o ID do voluntario a ser deletado: "))
                deletar_voluntario(id)
        elif op == '10':
                id = int(input("Digite o ID do veterinario a ser deletado: "))
                deletar_veterinario(id)
        elif op == '11':
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida! Tente novamente.")