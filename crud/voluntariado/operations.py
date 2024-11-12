import json, os

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")

def carregar_dados():
    try:
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_dados(dados):
    with open(DATA_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4)


def gerar_id_unico(dados):
    if not dados:
        return 1  
    else:
        maior_id = max(voluntario["id"] for voluntario in dados)
        return maior_id + 1

def adicionar_voluntario(nome,idade, contato, mes):
    dados = carregar_dados()
    novo_id = gerar_id_unico(dados) 
    novo_voluntario = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "contato": contato,
        "mes":mes
    }
    dados.append(novo_voluntario)
    salvar_dados(dados)
    print(f"Obrigado por se prestar a nos ajudar 🥰! ID: {novo_id}")
def adicionar_voluntario_veterinario(nome,contato, especialidade, dia):
    dados = carregar_dados()
    novo_id = gerar_id_unico(dados) 
    novo_veterinario = {
        "id": novo_id,
        "nome": nome,
        "contato": contato,
        "especialidade": especialidade,
        "dia":dia
    }
    dados.append(novo_veterinario)
    salvar_dados(dados)
    print(f"Obrigado por querer ajudar nossos pets 🥰! ID: {novo_id}")

def listar_voluntario():
    dados = carregar_dados()
    if not dados: 
        print("Nenhum voluntario encontrado.")
        return
    for voluntario in dados:
        print(f"ID: {voluntario['id']} - Nome: {voluntario['nome']}, Idade: {voluntario['idade']}")

def listar_veterinario():
    dados = carregar_dados()
    if not dados: 
        print("Nenhum voluntario encontrado.")
        return
    for veterinario in dados:
        print(f"ID: {veterinario['id']} - Nome: {veterinario['nome']}, Especialidade{veterinario['especialidade']}, Dia{veterinario['dia']}")
        
def atualizar_voluntario(id, novo_nome, nova_idade, novo_contato, novo_mes):
    dados = carregar_dados()
    for voluntatio in dados:
        if  voluntatio["id"] == id:
            voluntatio["nome"] = novo_nome
            voluntatio["idade"] = nova_idade
            voluntatio["contato"] = novo_contato
            voluntatio["mes"] = novo_mes 
            salvar_dados(dados)
            print("Voluntário atualizado com sucesso!")
            return
    print("Voluntário não encontrada.")

def atualizar_veterinario(id, novo_nome, nova_idade, novo_contato, novo_mes):
    dados = carregar_dados()
    for veterinario in dados:
        if  veterinario["id"] == id:
            veterinario["nome"] = novo_nome
            veterinario["idade"] = nova_idade
            veterinario["contato"] = novo_contato
            veterinario["mes"] = novo_mes   
            salvar_dados(dados)
            print("Veterinário atualizado com sucesso!")
            return
    print("Veterinário não encontrado.")

def buscar_voluntario(nome):
    dados = carregar_dados()
    resultados = [voluntario for voluntario in dados if voluntario["nome"].lower() == nome.lower()]
    if resultados:
        for voluntario in resultados:
            print(f"ID: {voluntario['id']} - Nome: {voluntario['nome']}, Espécie: {voluntario['especie']}, Raça: {voluntario['raca']}, Idade: {voluntario['idade']}, Personalidade: {voluntario['personalidade']}, Saúde: {voluntario['situacao_saude']}")
    else:
        print(f"Voluntário com nome '{nome}' não encontrado.")

def deletar_voluntario(id):
    dados = carregar_dados()
    dados = [voluntario for voluntario in dados if voluntario["id"] != id]
    salvar_dados(dados)
    print("Voluntário removido 😢")
def deletar_veterinario(id):
    dados = carregar_dados()
    dados = [veterinario for veterinario in dados if veterinario["id"] != id]
    salvar_dados(dados)
    print("Veterinário removido 😢")
    
