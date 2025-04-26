import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")

meanings = [
    ("O Louco",       "Novos começos, fé, espontaneidade.",    "Impulsividade e falta de direção."),
    ("O Mago",        "Habilidade, ação, poder de manifestação.", "Manipulação e falta de foco."),
    ("A Sacerdotisa", "Intuição, mistério, sabedoria interna.",  "Segredos revelados e desconfiança."),
    ("A Imperatriz",  "Abundância, fertilidade, nutrição.",      "Dependência e estagnação."),
    ("O Imperador",   "Autoridade, estrutura, liderança.",       "Tirania e inflexibilidade."),
    ("O Hierofante",  "Tradição, espiritualidade, conformidade.",  "Rebeldia e dogmatismo."),
    ("Os Enamorados", "Amor, escolha, harmonia.",                "Indecisão e conflitos."),
    ("O Carro",       "Determinação, vitória, controle.",       "Impaciência e agressividade."),
    ("A Justiça",     "Equilíbrio, verdade, responsabilidade.",  "Injustiça e desequilíbrio."),
    ("O Eremita",     "Introspecção, busca interior, sabedoria.", "Isolamento e solidão."),
    ("Roda da Fortuna","Ciclos, destino, oportunidades.",        "Resistência à mudança."),
    ("A Força",       "Coragem, autocontrole, compaixão.",       "Dúvidas e fraqueza interna."),
    ("O Enforcado",   "Sacrifício, nova perspectiva, entrega.",   "Teimosia e falta de progresso."),
    ("A Morte",       "Transformação, renascimento, fim de ciclo.", "Medo de mudança e estagnação."),
    ("Temperança",    "Equilíbrio, moderação, propósito.",       "Excessos e desequilíbrio."),
    ("O Diabo",       "Vícios, materialismo, sombras internas.",  "Libertação e superação de vícios."),
    ("A Torre",       "Ruptura súbita, revelação, libertação.",  "Medo de mudanças forçadas."),
    ("A Estrela",     "Esperança, inspiração, cura.",           "Desânimo e expectativas frustradas."),
    ("A Lua",         "Ilusões, intuição, medos ocultos.",      "Clareza e revelação de ilusões."),
    ("O Sol",         "Sucesso, vitalidade, clareza.",          "Esgotamento e superficialidade."),
    ("Julgamento",    "Renascimento, perdão, chamada interior.", "Arrependimento excessivo."),
    ("O Mundo",       "Conclusão, realização, plenitude.",      "Medo do próximo ciclo.")
]

tarot_deck = []
for i, (name, up, rev) in enumerate(meanings):
    tarot_deck.append({
        "name": f"{name} ({i})",
        "meaning_up": up,
        "meaning_rev": rev,
        "image_path": os.path.join(IMAGES_DIR, f"{i}.png")
    })
