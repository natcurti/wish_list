import subprocess, time, json, random

lista_itens = [] 

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
        print("Arquivo salvo com sucesso!")
    except Exception:
        print("Erro genérico não tratado")

def listar_itens(opcao):
    try:
        with open("wish_list.json", "r", encoding="utf-8") as arquivo:
            lista_itens = json.load(arquivo)
            if(len(lista_itens) == 0):
                print("Não há itens na sua wish list.")
            elif(opcao.upper() == 'TODOS'):
                listar_console(lista_itens)
            else: 
                pesquisar_categoria(opcao, lista_itens)
    except FileNotFoundError:
        print("Arquivo não encontrado")

def pesquisar_categoria(categoria, itens):
    itens_da_categoria = []
    for item in itens: 
        if(item["categoria"] == categoria):
            itens_da_categoria.append(item)
    
    if(len(itens_da_categoria) > 0):
        listar_console(itens_da_categoria)
    else:
        print("Não foram encontrados itens dessa categoria.")


def listar_console(itens):
    print(f"{'ID':>5} | {'NOME':<15} | {'CATEGORIA':<15} | {'DISPONIBILIDADE':<15}")
    for item in itens:
        print(f"{item["id"]:>5} | {item["nome"]:<15} | {item["categoria"]:<15} | {item["disponibilidade"]:<15}")
    

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

def validar_opcao_escolhida(opcao_escolhida, valor_inicial, valor_final):
    try: 
        opcao = int(opcao_escolhida)
        return opcao 
    except ValueError: 
        return f"Entrada inválida. Digite um número entre {valor_inicial} e {valor_final}"
    except Exception:
        return f"Erro genérico não identificado"
    
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
    opcao = validar_opcao_escolhida(opcao_digitada, 1, 6)
    
    match (opcao):
        case 1:
            nome = solicitar_e_validar_string("Digite o nome do item a ser adicionado: ")
            categoria = solicitar_e_validar_string("Digite a categoria do item: ")
            adicionar_item(nome, categoria)
            salvar_arquivo()
        case 2: 
            listar_itens("todos")
        case 3:
            categoria = solicitar_e_validar_string("Digite a categoria que deseja buscar: ")
            listar_itens(categoria)
            

            


    time.sleep(3)
    