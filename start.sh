#!/bin/bash

echo "🧙‍♂️ Iniciando EsoterIA..."

# Define o caminho do seu Python 3.10 instalado via Python.org
PYTHON_BIN="/Library/Frameworks/Python.framework/Versions/3.10/bin/python3"

# 1. Cria o venv se não existir
if [ ! -d "venv" ]; then
    echo "🔧 Criando ambiente virtual..."
    $PYTHON_BIN -m venv venv
fi

# 2. Ativa o venv
source ./venv/bin/activate

# 3. Instala dependências se necessário
if [ ! -f "venv_installed.flag" ]; then
    echo "📦 Instalando pacotes..."
    python -m pip install --upgrade pip
    $PIP install flask matplotlib pyqt5 pyswisseph pytz numpy reportlab
    touch venv_installed.flag
fi

# 4. Cria pasta de resultados se não existir
mkdir -p static/resultados

# 5. Roda o app
echo "🚀 Rodando o site EsoterIA!"
python app.py
