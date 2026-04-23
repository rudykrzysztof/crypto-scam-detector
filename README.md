# 🚨 Crypto Scam Detector

Tool do oceny ryzyka projektów kryptowalutowych na podstawie opisu, marketingu i prostych heurystyk.

## ✨ Features

* wykrywanie red flags w opisach projektów
* scoring ryzyka
* klasyfikacja: SAFE / RISKY / HIGH RISK / LIKELY SCAM
* prosty frontend webowy
* backend w Pythonie

## 🧠 Jak działa

Aplikacja analizuje tekst projektu i szuka wzorców często spotykanych w scamach, np.:

* guaranteed profit
* risk-free investment
* anonymous team
* limited time only
* 100x returns
* no audit
* instant passive income

Każda flaga zwiększa wynik ryzyka.

## 🚀 Start

```bash
pip install -r requirements.txt
python app.py
```

Potem otwórz:

```bash
http://127.0.0.1:5000
```

## 📊 Przykładowe zastosowania

* analiza landing page tokena
* sprawdzanie opisów presale
* edukacja użytkowników początkujących
* demo projektu do portfolio

## 🔮 Future improvements

* NLP model
* analiza whitepaperów
* integracja z realnymi API
* analiza strony projektu
* scam score visualization

## 📜 License

MIT
