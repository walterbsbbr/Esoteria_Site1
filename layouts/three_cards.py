from PyQt5.QtWidgets import QGridLayout, QGroupBox, QLabel, QTextEdit, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt

labels = ["Passado", "Presente", "Futuro"]

def setup(container, cards_list):
    """
    Monta o spread Três Cartas dentro de 'container'.
    cards_list deve ser passado vazio e receberá tuplas (img_lbl, name_lbl, mean_txt).
    """
    layout = QGridLayout(container)
    layout.setSpacing(20)

    # 1 linha × 3 colunas
    for c in range(3):
        layout.setColumnStretch(c, 1)
    layout.setRowStretch(0, 1)

    for idx, title in enumerate(labels):
        box = QGroupBox(title)
        box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        v = QVBoxLayout(box)

        # Imagem fixa em 200x300
        img = QLabel()
        img.setAlignment(Qt.AlignCenter)
        img.setFixedSize(200, 300)

        # Nome da carta
        name_lbl = QLabel("–", alignment=Qt.AlignCenter)
        name_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Significado resumido com altura fixa
        mean_txt = QTextEdit(readOnly=True)
        mean_txt.setFixedHeight(80)
        mean_txt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        v.addWidget(img, alignment=Qt.AlignCenter)
        v.addWidget(name_lbl)
        v.addWidget(mean_txt)

        layout.addWidget(box, 0, idx)
        cards_list.append((img, name_lbl, mean_txt))
