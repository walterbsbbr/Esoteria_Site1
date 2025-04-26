import unicodedata
import swisseph as swe
from datetime import datetime
import pytz
import numpy as np
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.table import Table

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
swe.set_ephe_path(os.path.join(BASE_DIR, "ephe"))
# Caminho para allCountries.txt
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "allCountries.txt")
FILE_URL = "https://drive.google.com/uc?export=download&id=19IpEg4tvPOT7eBepdfCR__ExctE59TQy"

# Garantir que o arquivo esteja presente
if not os.path.exists(FILE_PATH):
    print("🔽 Baixando allCountries.txt de Google Drive...")
    os.makedirs(DATA_DIR, exist_ok=True)
    response = requests.get(FILE_URL)
    if response.status_code == 200:
        with open(FILE_PATH, "wb") as f:
            f.write(response.content)
        print("✅ Download completo de allCountries.txt.")
    else:
        print(f"❌ Falha ao baixar (código {response.status_code})")
else:
    print("✅ allCountries.txt já está presente.")
    
    PLANETAS = {
    "☉": swe.SUN, "☽": swe.MOON, "☿": swe.MERCURY, "♀": swe.VENUS,
    "♂": swe.MARS, "♃": swe.JUPITER, "♄": swe.SATURN, "♅": swe.URANUS,
    "♆": swe.NEPTUNE, "♇": swe.PLUTO, "⚷": 15, "⚸": 12, "☊": swe.TRUE_NODE
}

ASPECTOS = {
    0: {"tol": 8, "cor": "red", "estilo": "solid", "simbolo": "☌"},
    30: {"tol": 3, "cor": "blue", "estilo": "dotted", "simbolo": "≿"},
    45: {"tol": 3, "cor": "red", "estilo": "dotted", "simbolo": "∕"},
    60: {"tol": 5, "cor": "blue", "estilo": "solid", "simbolo": "*"},
    90: {"tol": 5, "cor": "red", "estilo": "solid", "simbolo": "□"},
    120: {"tol": 5, "cor": "blue", "estilo": "solid", "simbolo": "△"},
    150: {"tol": 3, "cor": "red", "estilo": "dotted", "simbolo": "⨯"},
    180: {"tol": 8, "cor": "red", "estilo": "solid", "simbolo": "⊗"},
}

SIGNOS = ["♈","♉","♊","♋","♌","♍","♎","♏","♐","♑","♒","♓"]

def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto.lower())
        if unicodedata.category(c) != 'Mn'
    )

def buscar_localizacao_offline(nome_cidade):
    nome = normalizar(nome_cidade)
    with open("allCountries.txt", encoding="utf-8") as f:
        for linha in f:
            partes = linha.split("\t")
            if len(partes) > 5:
                nome_linha = normalizar(partes[1])
                if nome == nome_linha:
                    return float(partes[4]), float(partes[5])
    return None, None

def parse_data_e_hora(data_str, hora_str):
    formatos = ["%d/%m/%Y %H:%M", "%Y-%m-%d %H:%M"]
    entrada = f"{data_str} {hora_str}"
    for f in formatos:
        try:
            return datetime.strptime(entrada, f)
        except ValueError:
            continue
    raise ValueError(f"Formato de data inválido: {entrada}")

def gerar_mapa(nome, data, hora, cidade):
    try:
        dt = parse_data_e_hora(data, hora)
        tz = pytz.timezone("America/Sao_Paulo")
        dt_utc = tz.localize(dt).astimezone(pytz.utc)

        lat, lon = buscar_localizacao_offline(cidade)
        if lat is None:
            return None

        jd = swe.julday(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour + dt_utc.minute / 60.0)
        casas, ascmc = swe.houses(jd, lat, lon, b'P')
        asc = ascmc[0]
        mc = ascmc[1]

        pos = {}
        for simbolo, cod in PLANETAS.items():
            p, _ = swe.calc_ut(jd, cod)
            pos[simbolo] = p[0]
        pos["☋"] = (pos["☊"] + 180) % 360
        pos["ASC"] = asc
        pos["MC"] = mc

        output_dir = "static/resultados"
        os.makedirs(output_dir, exist_ok=True)
        filename = f"mapa_{normalizar(nome).replace(' ', '_')}.png"
        output_path = os.path.join(output_dir, filename)
        plotar_mapa(pos, casas, nome, data, output_path)
        return "/" + output_path

    except Exception as e:
        print("Erro ao gerar mapa:", e)
        return None

def plotar_mapa(pos, casas, nome, data_str, output_path):
    def formatar_graus(graus):
        total = graus % 30
        g = int(total)
        m = int((total - g) * 60)
        return f"{g}° {m:02d}′"

    fig = plt.figure(figsize=(14, 12))
    ax = fig.add_subplot(121, projection='polar')
    ax.set_theta_direction(-1)
    ax.set_theta_offset(np.pi / 2)
    ax.set_yticklabels([])
    ax.set_xticks([])

    fig.text(0.03, 0.96, nome, fontsize=16, fontweight='bold', ha='left')
    fig.text(0.03, 0.92, data_str, fontsize=14, ha='left')

    for i, sig in enumerate(SIGNOS):
        ang = 360 - (i * 30 + 15) + 90
        theta = np.radians(ang)
        x, y = np.cos(theta) * 0.84, np.sin(theta) * 0.84
        circle = Circle((x, y), 0.045, transform=ax.transData._b, facecolor='#fff8cc', edgecolor='none')
        ax.add_patch(circle)
        ax.text(theta, 0.84, sig, fontsize=22, fontweight='bold', ha='center', va='center')

    for i in range(12):
        grau = casas[i]
        theta = np.radians(360 - grau + 90)
        ax.plot([theta, theta], [0, 1], color='black', linewidth=1.8)
        ax.text(theta, 1.12, formatar_graus(grau), fontsize=8, ha='center', va='center')

    setores = {}
    for nome_p, grau in sorted(pos.items(), key=lambda x: x[1]):
        setor = int(grau)
        offset = setores.get(setor, 0)
        theta = np.radians(360 - grau + 90)
        ax.text(theta, 1.05 - offset * 0.07, nome_p, fontsize=15, fontweight='bold', ha='center')
        setores[setor] = offset + 1

    chaves = list(pos.keys())
    for i in range(len(chaves)):
        for j in range(i + 1, len(chaves)):
            a1, a2 = pos[chaves[i]], pos[chaves[j]]
            diff = abs(a1 - a2) % 360
            for grau, cfg in ASPECTOS.items():
                if abs(diff - grau) <= cfg['tol']:
                    t1 = np.radians(360 - a1 + 90)
                    t2 = np.radians(360 - a2 + 90)
                    ax.plot([t1, t2], [1, 1], color=cfg['cor'], linestyle=cfg['estilo'], alpha=0.6, linewidth=1)
                    break

    ax2 = fig.add_subplot(222)
    ax2.set_axis_off()
    tabela = Table(ax2, bbox=[0, 0, 1, 1])
    nomes = list(pos.keys())
    n = len(nomes)
    cw = 1.0 / (n + 1)
    ch = 1.0 / (n + 1)

    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                tabela.add_cell(i, j, cw, ch, text="", loc='center')
            elif i == 0:
                tabela.add_cell(i, j, cw, ch, text=nomes[j - 1], loc='center', facecolor='#f0f0f0')
            elif j == 0:
                tabela.add_cell(i, j, cw, ch, text=nomes[i - 1], loc='center', facecolor='#f0f0f0')
            elif j < i:
                ang = abs(pos[nomes[i - 1]] - pos[nomes[j - 1]]) % 360
                simbolo = ""
                color = "black"
                for grau, cfg in ASPECTOS.items():
                    if abs(ang - grau) <= cfg['tol']:
                        simbolo = cfg['simbolo']
                        color = cfg['cor']
                        break
                cell = tabela.add_cell(i, j, cw, ch, text=simbolo, loc='center', facecolor='white')
                cell.get_text().set_color(color)
            else:
                tabela.add_cell(i, j, cw, ch, text="", loc='center', facecolor='lightgrey')
    ax2.add_table(tabela)

    # Tabela 3 – posições
    ax3 = fig.add_axes([0.51, 0.05, 0.45, 0.35])
    ax3.set_axis_off()
    tabela_pos = Table(ax3, bbox=[0, 0, 1, 1])
    row_height = 1.0 / (len(nomes) + 1)
    tabela_pos.add_cell(0, 0, 0.5, row_height, text="Planeta", loc='center', facecolor='#f0f0f0')
    tabela_pos.add_cell(0, 1, 0.5, row_height, text="Posição", loc='center', facecolor='#f0f0f0')

    for i, nome_p in enumerate(nomes):
        grau = pos[nome_p]
        sig = SIGNOS[int(grau // 30)]
        g = int(grau % 30)
        m = int((grau % 1) * 60)
        grau_fmt = f"{g}° {m:02d}′"
        tabela_pos.add_cell(i + 1, 0, 0.5, row_height, text=nome_p, loc='center')
        tabela_pos.add_cell(i + 1, 1, 0.5, row_height, text=f"{grau_fmt} {sig}", loc='center')

    ax3.add_table(tabela_pos)

    plt.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
