import time

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