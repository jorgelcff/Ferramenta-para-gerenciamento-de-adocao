import os
def menu_principal():
    print('''
█▀▀ █▀▀ █▀ ▄▀█ █▀█ ▀ █▀   ▄▀█ █▄░█ █ █▀▄▀█ ▄▀█ █░░   █░█ █░█ █▄▄
█▄▄ ██▄ ▄█ █▀█ █▀▄ ░ ▄█   █▀█ █░▀█ █ █░▀░█ █▀█ █▄▄   █▀█ █▄█ █▄█\n''')
    print("1. Gerenciamento de Adoção de Animais")
    print("2. Gerenciamento de Clientes")
    print("3. Pet Shop")
    print("4. Voluntariado")
    print("5. Sair")

def main():
    while True:
        menu_principal()
        op = input("Escolha a opção desejada: ")

        if op == '1':
            import adocao.init as adocao
            os.system("cls")
            adocao.main()
        elif op == '2':
            import cliente.init as cliente
            os.system("cls")
            cliente.main()
        elif op == '3':
            import pet_shop.init as pet_shop
            os.system("cls")
            pet_shop.main()
        elif op == '4':
            import voluntariado.init as voluntariado
            os.system("cls")
            voluntariado.main()
        elif op == '5':
            print("Saindo do sitema... ")
            break
        else:
            print("Opção inválida! Tente novamente. ")

if __name__ == "__main__":
    main()




       