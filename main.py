import subprocess, time, json, random, os

lista_itens = [] 

try:
    with open("wish_list.json", "r", encoding="utf-8") as arquivo:
        lista_itens = json.load(arquivo)
except FileNotFoundError:
    lista_itens = []
    with open("wish_list.json", "w", encoding="utf-8", ensure_ascii=False) as arquivo:
        json.dump(lista_itens, arquivo, indent=4) 

def adicionar_item(nome, categoria):
    id_item = len(lista_itens) + 1
    disponibilidade = random.choice(["Disponível", "Indisponível"])
    item_para_add = {
        "id": id_item,
        "nome": nome,
        "categoria": categoria,
        "disponibilidade": disponibilidade 
    }
    lista_itens.append(item_para_add)
    print("Item adicionado com sucesso!")

def salvar_arquivo():
    try:
        with open("wish_list.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista_itens, arquivo, indent=4, ensure_ascii=False)
    except Exception:
        print("Erro genérico não tratado")

def ler_arquivo():
    try:
        with open("wish_list.json", "r", encoding="utf-8") as arquivo:
            lista_itens = json.load(arquivo)
            if(len(lista_itens) == 0):
                print("Não há itens na sua wish list.")
            else:
                return lista_itens
    except FileNotFoundError:
        print("Arquivo não encontrado")

def listar_todos():
    lista_itens = ler_arquivo()
    if(lista_itens):
        listar_console(lista_itens)
    
def pesquisar_categoria(categoria):
    lista_itens = ler_arquivo()
    itens_da_categoria = []
    for item in lista_itens: 
        if(item["categoria"] == categoria):
            itens_da_categoria.append(item)
    
    if(len(itens_da_categoria) > 0):
        listar_console(itens_da_categoria)
    else:
        print("Não foram encontrados itens dessa categoria.")

def remover_item(id):
    lista_itens = ler_arquivo()
    for index, item in enumerate(lista_itens, start=0):
        if(item["id"] == id):
            del lista_itens[index]
    
    print("Item removido com sucesso da lista!")
    salvar_arquivo()


def listar_console(itens):
    subprocess.run(["cls"], shell=True)
    print(f"{'ID':>5} | {'NOME':<15} | {'CATEGORIA':<15} | {'DISPONIBILIDADE':<15}")
    for item in itens:
        print(f"{item["id"]:>5} | {item["nome"]:<15} | {item["categoria"]:<15} | {item["disponibilidade"]:<15}")

def verificar_disponibilidade(nome):
    itens = ler_arquivo()
    itens_encontrados = []
    for item in itens:
        if(item["nome"].upper() == nome.upper()):
            itens_encontrados.append(item)
    
    if(len(itens_encontrados) > 0):
        for item in itens_encontrados:
            print(f"O item {item["nome"]} de id {item["id"]} está {item["disponibilidade"]}")
    else:
        print("Não há itens cadastrados com este nome em sua wish list")


def exibir_menu():
    subprocess.run(["cls"], shell=True)
    opcoes = ["Adicionar Item", "Listar Todos", "Listar por Categoria", "Verificar disponibilidade", "Remover Item", "Sair"]

    print(
        """ 
        Bem vindo(a) ao app:

        ░██╗░░░░░░░██╗██╗░██████╗██╗░░██╗  ██╗░░░░░██╗░██████╗████████╗
        ░██║░░██╗░░██║██║██╔════╝██║░░██║  ██║░░░░░██║██╔════╝╚══██╔══╝
        ░╚██╗████╗██╔╝██║╚█████╗░███████║  ██║░░░░░██║╚█████╗░░░░██║░░░
        ░░████╔═████║░██║░╚═══██╗██╔══██║  ██║░░░░░██║░╚═══██╗░░░██║░░░
        ░░╚██╔╝░╚██╔╝░██║██████╔╝██║░░██║  ███████╗██║██████╔╝░░░██║░░░
        ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚══════╝╚═╝╚═════╝░░░░╚═╝░░░
        """
    )

    for index, opcao in enumerate(opcoes, start=1):
        print(f"{index}. {opcao}")

def validar_inteiro(opcao_escolhida, valor_inicial=None, valor_final=None):
    try: 
        opcao = int(opcao_escolhida)
        return opcao 
    except ValueError: 
        if(valor_inicial and valor_final):
            print(f"Entrada inválida. Digite um número entre {valor_inicial} e {valor_final}")
        else:
            print(f"Entrada inválida. Digite um id válido")
    except Exception:
        print(f"Erro genérico não identificado")
    
def solicitar_e_validar_string(frase_input):
    while True:
        resposta = input(frase_input)
        if(len(resposta.strip()) > 3):
            return resposta
        else:
            print("Entrada inválida. Digite uma entrada válida com no mínimo 3 caracteres.")
            time.sleep(2)
    
while True:
    exibir_menu()
    opcao_digitada = input("Digite a opção escolhida: ")
    opcao = validar_inteiro(opcao_digitada, 1, 6)
    
    match (opcao):
        case 1:
            nome = solicitar_e_validar_string("Digite o nome do item a ser adicionado: ")
            categoria = solicitar_e_validar_string("Digite a categoria do item: ")
            adicionar_item(nome, categoria)
            salvar_arquivo()
        case 2: 
            listar_todos()
        case 3:
            categoria = solicitar_e_validar_string("Digite a categoria que deseja buscar: ")
            pesquisar_categoria(categoria)
        case 4:
            nome = solicitar_e_validar_string("Digite o nome do item que deseja procurar: ")
            verificar_disponibilidade(nome)
        case 5: 
            id = input("Digite o id do produto para remover: ")
            id_para_buscar = validar_inteiro(id)
            if id_para_buscar:
                remover_item(id_para_buscar)


    time.sleep(3)
    