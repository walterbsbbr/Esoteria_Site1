from PyQt5.QtWidgets import (
    QHBoxLayout, QGridLayout, QGroupBox, QLabel, QTextEdit,
    QVBoxLayout, QSizePolicy, QWidget
)
from PyQt5.QtCore import Qt

# Posições fixas da Cruz Celta em grid 6 linhas x 5 colunas
positions = {
    0: (1, 2),  # Significador
    1: (1, 3),  # Cruzar
    2: (2, 2),  # Fundação
    3: (1, 1),  # Passado
    4: (0, 2),  # Objetivo
    5: (1, 4),  # Futuro
    6: (2, 4),  # Você
    7: (3, 4),  # Ambiente
    8: (4, 4),  # Esperanças e Medos
    9: (5, 4)   # Resultado
}

labels = [
    "Significador", "Cruzar", "Fundação", "Passado", "Objetivo",
    "Futuro", "Você", "Ambiente", "Esperanças e Medos", "Resultado"
]

def setup(container, cards_list):
    """
    Monta o spread Cruz Celta dentro de 'container', alinhado conforme 'outer.setAlignment'.
    cards_list: lista que receberá tuplas (img_lbl, name_lbl, mean_txt).
    """
    # Layout externo para alinhar o grid dentro do container
    outer = QHBoxLayout(container)
    outer.setContentsMargins(3, 3, 3, 3)
    outer.setSpacing(3)
    outer.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # <-- aqui você ajusta o alinhamento

    # Widget interno que conterá o grid
    grid_widget = QWidget()
    grid_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    outer.addWidget(grid_widget)

    # Grid 6x5 dentro do widget interno
    layout = QGridLayout(grid_widget)
    layout.setSpacing(5)

    # Stretch igualitário nas linhas apenas
    for r in range(6):
        layout.setRowStretch(r, 1)

    # Cria cada slot reduzido
    for idx, title in enumerate(labels):
        r, c = positions[idx]
        box = QGroupBox(title)
        box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        v = QVBoxLayout(box)
        v.setContentsMargins(2, 2, 2, 2)
        v.setSpacing(2)

        # Imagem compacta para caber na tela
        img = QLabel()
        img.setAlignment(Qt.AlignCenter)
        img.setFixedSize(50, 75)

        # Nome da carta
        name_lbl = QLabel("–", alignment=Qt.AlignCenter)
        name_lbl.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Significado resumido pequeno
        mean_txt = QTextEdit(readOnly=True)
        mean_txt.setFixedHeight(30)
        mean_txt.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        v.addWidget(img, alignment=Qt.AlignCenter)
        v.addWidget(name_lbl)
        v.addWidget(mean_txt)

        layout.addWidget(box, r, c)
        cards_list.append((img, name_lbl, mean_txt))
