from flask import Flask, render_template, request, send_file, redirect
import os
import Astro
import ic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/astrologia', methods=['GET', 'POST'])
def astrologia():
    mapa_path = None
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['data']
        hora = request.form['hora']
        cidade = request.form['cidade']
        mapa_path = Astro.gerar_mapa(nome, data, hora, cidade)
    return render_template('astrologia.html', mapa_path=mapa_path)

@app.route('/iching', methods=['GET', 'POST'])
def iching():
    resultado = None
    erro = None
    if request.method == 'POST':
        resultado = ic.sortear()
        if "erro" in resultado:
            erro = resultado["erro"]
            resultado = None
    return render_template("iching.html", resultado=resultado, erro=erro)

@app.route('/tarot', methods=['GET', 'POST'])
def tarot():
    from tarot_deck import tarot_deck
    import random

    posicoes = ["Passado", "Presente", "Futuro"]
    cartas_sorteadas = random.sample(tarot_deck, 3)
    cartas = []

    for i, carta in enumerate(cartas_sorteadas):
        invertida = random.choice([True, False])
        cartas.append({
            "nome": carta["name"],
            "img": os.path.basename(carta["image_path"]),
            "significado": carta["meaning_rev"] if invertida else carta["meaning_up"],
            "invertida": invertida,
            "posicao": posicoes[i]
        })

    return render_template("tarot.html", cartas=cartas)


if __name__ == '__main__':
    app.run(debug=True)
