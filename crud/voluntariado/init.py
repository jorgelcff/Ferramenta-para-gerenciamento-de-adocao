from voluntariado.operations import adicionar_voluntario, adicionar_voluntario_veterinario, listar_voluntario, listar_veterinario, deletar_veterinario, deletar_voluntario
import os 

def menu_voluntariado():
    print("===== Venha fazer parte do nosso time =====")
    print("1. Cadastro pessoa voluntaria")
    print("2. Cadastro veterinario voluntario")
    print("3. Listar pessoas voluntarias e seus dias")
    print("4. Listar veterinarios voluntarios e seus dias")
    print("5. buscar pessoa voluntaria")
    print("6. buscar veterinario voluntario")
    print("7. Remover pessoa voluntaria")
    print("8. Remover veterinario voluntario")
    print("9. Voltar ao Menu Principal")

def main():
    while True:
        menu_voluntariado()
        op = input("Escolha a opção: ")
        if op == '1':
            nome = input("Digite seu nome: ")
            idade = input("Digite sua idade ")
            if idade <18:
                print("infelizmente não estamos aceitando voluntarios menores de idade no momento, agradecemos por querer ajudar 🥰 ")
                break
            contato = input("Digite seu email para contato:")
            mes = input("Digite a quantidade de vezes que podera comparecer para ser voluntario no mês")
            adicionar_voluntario(nome, idade, contato, mes)
            
        elif op =='2':
            nome = input("Digite seu nome: ")
            contato = input("Digite seu email para contato:")
            especialidade = input("Digite sua expecialidade:")
            dia = input("Digite o dia que podera atender:")
            horario = input("digite o horario que poderá atender:")
            adicionar_voluntario_veterinario(nome, contato, especialidade, dia, horario)
        elif op == '3':
            listar_voluntario()
        elif op == '4':
            listar_veterinario()
        elif op =='5':
            
        elif op =='6':
            
        elif op == '7':
                id = int(input("Digite o ID do voluntario a ser deletado: "))
                deletar_voluntario(id)
        elif op == '8':
                id = int(input("Digite o ID do veterinario a ser deletado: "))
                deletar_veterinario(id)
        elif op == '9':
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida! Tente novamente.")