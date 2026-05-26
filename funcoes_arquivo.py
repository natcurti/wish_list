import json

def verificar_arquivo_existe():
    try:
        with open("wish_list.json", "r", encoding="utf-8") as arquivo:
            lista_itens = json.load(arquivo)
    except FileNotFoundError:
        lista_itens = []
        with open("wish_list.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista_itens, arquivo, indent=4, ensure_ascii=False) 
    return lista_itens

def salvar_arquivo(lista_itens):
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