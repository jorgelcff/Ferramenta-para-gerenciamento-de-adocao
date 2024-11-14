from voluntariado.operations import adicionar_voluntario, adicionar_voluntario_veterinario, listar_voluntario, listar_veterinario, atualizar_voluntario, atualizar_veterinario, buscar_voluntario, buscar_veterinario, deletar_veterinario, deletar_voluntario
import os 

def menu_voluntariado():
    print("===== Venha fazer parte do nosso time!! =====")
    print("1. Cadastro para voluntário(a) geral")
    print("2. Cadastro para voluntário(a) médico(a)")
    print("3. Listar voluntário(a) geral")
    print("4. Listar voluntário(a) médico(a)")
    print("5. Atualizar voluntário(a) geral")
    print("6. Atualizar voluntário(a) médico(a)")
    print("7. Buscar voluntário(a) geral")
    print("8. Buscar voluntário(a) médico(a)")
    print("9. Remover voluntário(a) geral")
    print("10. Remover voluntário(a) médico(a)")
    print("11. Voltar ao Menu Principal")

def invalido():
    print("Opção invalida tente novamente")

def main():
    while True:
        try:
            menu_voluntariado()
            op = input("Escolha uma das opções: ")
            if op == '1':
                nome = input("Digite seu nome: ")
                idade = int(input("Digite sua idade: "))
                if idade <18:
                    print("Infelizmente não estamos aceitando voluntário(a)s menores de idade no momento, agradecemos por querer ajudar!! 🥰 ")
                    break
                contato = input("Digite seu melhor email para contato:")
                mes = int(input("Digite a quantidade de vezes que poderá comparecer para ser voluntário(a) no mês: "))
                adicionar_voluntario(nome, idade, contato, mes)
            
            elif op =='2':
                nome = input("Digite seu nome: ")
                contato = input("Digite seu melhor email para contato: ")
                especialidade = input("Digite sua especialidade: ")
                dia = int(input("Digite o dia que poderá atender: "))
                
                adicionar_voluntario_veterinario(nome, contato, especialidade, dia)
                
            elif op == '3':
                 listar_voluntario()
                 
            elif op == '4':
                 listar_veterinario()

            elif op =='5':
                id = int(input("Digite o ID do voluntário(a) a ser atualizado: "))
                novo_nome = input("Digite o novo nome do voluntário(a): ")
                nova_idade = input("Digite a nova idade do voluntário(a): ")
                novo_contato = input("Digite o novo contato do(a) voluntário(a): ")
                novo_mes = int(input("Digite a nova disponibilidade (quantas vezes poderá ajudar no mês) do(a) voluntário(a): "))
                
                atualizar_voluntario(id, novo_nome, nova_idade, novo_contato, novo_mes)

            elif op =='6':
                id = int(input("Digite o ID do(a) veterinário(a) a ser atualizado: "))
                novo_nome = input("Digite o novo nome do(a) veterinário(a): ")
                nova_idade = input("Digite a nova idade do(a) veterinário(a): ")
                novo_contato = input("Digite o contato do(a) veterinário(a): ")
                novo_dia = int(input("Digite o novo dia de disponibilidade do(a) veterinário(a): "))
                
                atualizar_veterinario(id, novo_nome, nova_idade, novo_contato, novo_dia)
             
            elif op =='7':
                nome = input("Digite o nome do(a) voluntário(a) que você deseja encontrar: ")
                
                buscar_voluntario(nome=nome)
             
            elif op =='8':
                nome = input("Digite o nome do(a) voluntário(a) que você deseja encontrar: ")
                
                buscar_veterinario(nome=nome)
            
            elif op == '9':
                id = int(input("Digite o ID do(a) voluntário(a) a ser deletado(a): "))
                deletar_voluntario(id)

            elif op == '10':
                id = int(input("Digite o ID do(a) veterinário(a) a ser deletado(a): "))
                deletar_veterinario(id)

            elif op == '11':
                print("Voltando ao menu principal...")
                break

            else:
                print("Opção inválida! Tente novamente.")
        except:
            invalido()
