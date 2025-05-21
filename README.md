# EsoterIA: A Web-Based Divination Toolkit

EsoterIA is a Python-based web application built with Flask that provides users with tools for divination and introspection. It currently features:

*   Astrological birth chart generation
*   I Ching readings
*   Tarot card readings

## Features

### 1. Astrology (Natal Chart Generation)

*   **Functionality:** Generates a visual natal (birth) chart based on the user's name, birth date, time, and city.
*   **Details:**
    *   Calculates planetary positions and house cusps (Placidus system).
    *   Displays aspects between planets (conjunction, sextile, square, trine, opposition, etc.) and their orbs.
    *   Lists planetary positions in zodiac signs and degrees.
    *   The application uses the `swisseph` library for precise astronomical calculations and `matplotlib` for rendering the chart as a PNG image.
    *   City coordinates are looked up locally, and the necessary data file (`allCountries.txt`) is automatically downloaded from Google Drive if not found.
*   **Input:** Name, Date of Birth, Time of Birth, City of Birth.
*   **Output:** A PNG image of the astrological chart and tables detailing planetary positions and aspects.

### 2. I Ching (Oracle Consultation)

*   **Functionality:** Simulates an I Ching reading using the yarrow stalk or coin toss method (implemented via random coin simulation).
*   **Details:**
    *   Generates six lines to form a primary hexagram.
    *   Identifies any changing lines (lines with values of 6 or 9) which transform the primary hexagram into a resultant hexagram.
    *   Provides interpretations for the primary hexagram, any changing lines, and the resultant hexagram.
    *   Hexagram texts, ideograms, judgments, images, and line meanings are sourced from local JSON files (`data/hexagramas.json` and `data/ideogramas.json`).
*   **Input:** User initiates the casting process (no specific data input required beyond the action).
*   **Output:** The primary hexagram, resultant hexagram (if any), their names, titles, ideograms, judgments, images, and the interpretation of any changing lines.

### 3. Tarot Reading (Three-Card Spread)

*   **Functionality:** Performs a simple three-card Tarot reading.
*   **Details:**
    *   Draws three cards randomly from a standard 22-card Major Arcana deck.
    *   Each card can be upright or reversed, affecting its interpretation.
    *   The three cards represent:
        1.  **Passado (Past):** Influences and events from the past.
        2.  **Presente (Present):** Current situation and energies.
        3.  **Futuro (Future):** Potential outcomes or future trends.
    *   Card names, meanings (upright and reversed), and images are defined in `tarot_deck.py`. Images are located in `static/images/`.
*   **Input:** User initiates the reading (no specific data input required).
*   **Output:** Displays the three drawn cards with their images, names, their position in the spread (Past, Present, Future), and their respective meanings (adjusted for upright/reversed).

## Project Structure

The project is organized as follows:

```
.
├── app.py            # Main Flask application: handles routing and web requests.
├── Astro.py          # Logic for astrological chart calculations and plotting.
├── ic.py             # Logic for I Ching casting and interpretation.
├── tarot_deck.py     # Defines the Tarot card deck, meanings, and image paths.
├── requirements.txt  # Lists Python package dependencies.
├── start.sh          # Shell script to run the application (likely for deployment/dev ease).
├── data/
│   ├── hexagramas.json # Data for I Ching hexagrams (names, titles, texts).
│   ├── ideogramas.json # Data for I Ching ideograms.
│   └── allCountries.txt# Geodata for city lookups (downloaded automatically if missing).
├── ephe/             # Directory containing Swiss Ephemeris data files for `swisseph`.
├── layouts/          # Contains PyQt5 UI layout code (seems to be for a separate desktop application or feature, not used by the web app).
│   ├── astrological.py
│   ├── celtic_cross.py
│   └── three_cards.py
├── static/
│   ├── images/       # Tarot card images (0.png, 1.png, etc.).
│   ├── moedas/       # Images for I Ching coins (cara.png, coroa.png).
│   ├── resultados/   # Sample pre-generated results (charts, hexagrams).
│   └── style.css     # CSS styles for the web application.
└── templates/
    ├── index.html    # Main landing page template.
    ├── astrologia.html # Template for the Astrology section.
    ├── iching.html   # Template for the I Ching section.
    └── tarot.html    # Template for the Tarot section.
```

## Setup and Installation

Follow these steps to set up and run the EsoterIA application locally:

1.  **Prerequisites:**
    *   Python 3.x
    *   Pip (Python package installer)
    *   Git (for cloning the repository)

2.  **Clone the Repository:**
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL
    cd <repository_directory_name>
    ```

3.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    Ensure your virtual environment is activated, then install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    The main dependencies include: `Flask`, `pyswisseph`, `pytz`, `numpy`, and `matplotlib`.

5.  **Ephemeris and Geodata Files:**
    *   The application requires Swiss Ephemeris files, which are included in the `ephe/` directory.
    *   It also uses a city lookup file (`data/allCountries.txt`). If this file is not present when you first run the astrology feature, the application will attempt to download it automatically from a predefined Google Drive link (requires an internet connection for the first download).

## Running the Application

1.  **Activate Virtual Environment:**
    If you haven't already, activate your virtual environment:
    *   On Windows: `.\venv\Scripts\activate`
    *   On macOS and Linux: `source venv/bin/activate`

2.  **Run the Flask Development Server:**
    ```bash
    python app.py
    ```

3.  **Access the Application:**
    Open your web browser and navigate to:
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

    You should see the EsoterIA application's home page.

**Note on `start.sh`:**
The `start.sh` script in the repository is likely configured to run the application using `gunicorn`, which is a more production-ready WSGI server. For development, `python app.py` is typically sufficient. If you intend to deploy the application, you might adapt or use the `start.sh` script. Example content of `start.sh` might be:
```bash
#!/bin/bash
# (Ensure gunicorn is installed: pip install gunicorn)
# Deactivate any existing virtual environment if necessary
# source venv/bin/activate # Or your specific activation path
gunicorn --workers 3 --bind 0.0.0.0:8000 app:app
```
(The actual content of `start.sh` in your project should be checked for specific deployment configurations.)

## Usage

Once the application is running, you can access its features through your web browser:

*   **Home Page (`/`):** The main landing page with links to the different sections.
*   **Astrology (`/astrologia`):**
    1.  Navigate to the "Astrologia" section.
    2.  Fill in the form with the required birth details (Name, Date, Time, City).
    3.  Click "Gerar Mapa" (Generate Chart).
    4.  The generated natal chart image will be displayed below the form.
*   **I Ching (`/iching`):**
    1.  Navigate to the "I Ching" section.
    2.  Click the button to perform the coin casting (e.g., "Sortear Hexagrama" or similar).
    3.  The results will be displayed, showing the primary hexagram, any changing lines with their interpretations, and the resultant hexagram. Details include names, titles, ideograms, judgments, and images.
*   **Tarot (`/tarot`):**
    1.  Navigate to the "Tarot" section.
    2.  The three-card spread (Past, Present, Future) will be automatically drawn and displayed.
    3.  Each card will show its image, name, position, and meaning (adjusted for whether it's upright or reversed).

## A Note on the `layouts/` Directory

The `layouts/` directory contains Python files (`astrological.py`, `celtic_cross.py`, `three_cards.py`) that use the `PyQt5` library. This code appears to be for creating UI layouts for a desktop application.

**Important:** This `PyQt5` code is not used by the main Flask web application (`app.py`) and seems to be part of a separate project or an earlier/alternative version of EsoterIA. The web application's interface is defined by the HTML files in the `templates/` directory.
