
import json
import random
import os

# Caminhos para os arquivos dentro da pasta 'data'
BASE_DIR = os.path.dirname(__file__)
CAMINHO_HEXAGRAMAS = os.path.join(BASE_DIR, 'data', 'hexagramas.json')
CAMINHO_IDEOGRAMAS = os.path.join(BASE_DIR, 'data', 'ideogramas.json')

VALOR_CARA = 3  # valor da moeda com dragão
VALOR_COROA = 2  # valor da moeda com ideogramas
mutantes = [6, 9]  # 6 e 9 são linhas mutantes

# Binários para hexagramas - formato: linha de baixo para cima (como no I Ching tradicional)
correspondencia_hexagramas = {
    '777777': 1, '888888': 2, '788878': 3, '878887': 4, '777878': 5, '878777': 6,
    '878888': 7, '888878': 8, '777877': 9, '778777': 10, '777888': 11, '888777': 12,
    '787777': 13, '777787': 14, '887888': 15, '888788': 16, '788887': 17, '877887': 18,
    '887888': 19, '888877': 20, '788787': 21, '787887': 22, '888887': 23, '788888': 24,
    '788777': 25, '777887': 26, '788887': 27, '877778': 28, '878878': 29, '787787': 30,
    '887778': 31, '877788': 32, '887777': 33, '777788': 34, '888787': 35, '787888': 36,
    '787877': 37, '778787': 38, '887878': 39, '878788': 40, '778887': 41, '788877': 42,
    '777778': 43, '877777': 44, '888778': 45, '877888': 46, '878778': 47, '877878': 48,
    '787778': 49, '877787': 50, '788788': 51, '887887': 52, '887877': 53, '778788': 54,
    '787788': 55, '887787': 56, '877877': 57, '778778': 58, '878877': 59, '778878': 60,
    '778877': 61, '887788': 62, '787878': 63, '878787': 64
}

def carregar_hexagramas():
    with open(CAMINHO_HEXAGRAMAS, encoding="utf-8") as f:
        return json.load(f)

def carregar_ideogramas():
    with open(CAMINHO_IDEOGRAMAS, encoding="utf-8") as f:
        return json.load(f)

def linha_para_primario(l):
    return '7' if l in [7, 9] else '8'  # 9 e 7 são yang (fechadas), 6 e 8 são yin (abertas)

def linha_para_resultante(l):
    if l == 6:
        return '7'
    elif l == 9:
        return '8'
    return linha_para_primario(l)

def sortear():
    hexagramas = carregar_hexagramas()
    ideogramas = carregar_ideogramas()

    moedas = []
    linhas = []

    for _ in range(6):
        trio = [random.choice([VALOR_CARA, VALOR_COROA]) for _ in range(3)]
        total = sum(trio)
        moedas.append(trio)
        linhas.append(total)

    bin_primario = ''.join([linha_para_primario(l) for l in linhas])
    bin_resultante = ''.join([linha_para_resultante(l) for l in linhas])

    primario_num = correspondencia_hexagramas.get(bin_primario, 1)
    resultante_num = correspondencia_hexagramas.get(bin_resultante, 2)

    primario = hexagramas[str(primario_num)]
    resultante = hexagramas[str(resultante_num)]

    mutantes_texto = []
    for i, linha in enumerate(linhas):
        if linha in mutantes:
            numero_linha = str(6 - i)
            texto = primario.get("linhas", {}).get(numero_linha)
            if texto:
                mutantes_texto.append(f"Linha {numero_linha}: {texto}")

    return {
        "linhas": linhas,
        "moedas": moedas,
        "linhas_mutantes_texto": mutantes_texto,
        "primario": {
            "numero": primario_num,
            "nome": primario["nome"],
            "titulo": primario["titulo"],
            "ideograma": ideogramas[str(primario_num)],
            "julgamento": primario["julgamento"],
            "imagem": primario["imagem"],
            "comentario": primario["comentario"]
        },
        "resultante": {
            "numero": resultante_num,
            "nome": resultante["nome"],
            "titulo": resultante["titulo"],
            "ideograma": ideogramas[str(resultante_num)],
            "julgamento": resultante["julgamento"],
            "imagem": resultante["imagem"],
            "comentario": resultante["comentario"]
        }
    }
