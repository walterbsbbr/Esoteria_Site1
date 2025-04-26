from PyQt5.QtWidgets import (
    QGridLayout, QGroupBox, QLabel, QTextEdit, QVBoxLayout, QSizePolicy
)
from PyQt5.QtCore import Qt

# Rótulos e significados das 12 casas
labels = [f"Casa {i+1}" for i in range(12)]
house_meanings = [
    "Identidade, aparência e modo de agir.",
    "Valores pessoais, finanças e posses.",
    "Comunicação, vizinhança e aprendizado.",
    "Família, lar e raízes.",
    "Prazer, criatividade e filhos.",
    "Trabalho, serviço e saúde.",
    "Parcerias, casamento e acordos.",
    "Transformação e recursos compartilhados.",
    "Viagens longas, fé e filosofia.",
    "Carreira, reputação e autoridade.",
    "Amizades, grupos e esperanças futuras.",
    "Inconsciente, espiritualidade e isolamento."
]

def setup(container, cards_list):
    """
    Monta o spread Astrológico dentro de 'container'.
    cards_list: lista que receberá tuplas (img_lbl, name_lbl, mean_txt).
    """
    # Cria um grid de 1 linha x 12 colunas
    layout = QGridLayout(container)
    layout.setSpacing(8)

    # Stretch igualitário para cada coluna
    for col in range(len(labels)):
        layout.setColumnStretch(col, 1)
    layout.setRowStretch(0, 1)

    # Popula cada célula
    for idx, title in enumerate(labels):
        # Caixa com título da casa
        box = QGroupBox(title)
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        v = QVBoxLayout(box)

        # 1) Significado estático da casa
        desc = QLabel(house_meanings[idx], alignment=Qt.AlignCenter)
        desc.setWordWrap(True)
        desc.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        desc.setStyleSheet("font-size:9pt; color: black;")

        # 2) Imagem da carta (vazia até o sorteio)
        img = QLabel()
        img.setAlignment(Qt.AlignCenter)
        img.setFixedSize(100, 150)

        # 3) Nome da carta (dinâmico)
        name_lbl = QLabel("–", alignment=Qt.AlignCenter)
        name_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # 4) Significado da carta (dinâmico)
        mean_txt = QTextEdit(readOnly=True)
        mean_txt.setFixedHeight(160)
        mean_txt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Adiciona à caixa
        v.addWidget(desc)
        v.addWidget(img, alignment=Qt.AlignCenter)
        v.addWidget(name_lbl)
        v.addWidget(mean_txt)

        # Insere no grid
        layout.addWidget(box, 0, idx)

        # Guarda referências para o main.py manipular depois
        cards_list.append((img, name_lbl, mean_txt))
