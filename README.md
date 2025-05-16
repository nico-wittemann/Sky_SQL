# ✈️ Sky SQL – Flight Data Explorer (CLI · SQLite · SQLAlchemy)

A command-line tool to explore and filter flight delay data from a local SQLite database using **raw SQL** and **SQLAlchemy Core**. Includes filters by airline, airport, date, and flight ID.

---

## 💡 Features

- Search flights by:
  - Flight ID
  - Date (day, month, year)
  - Origin Airport (IATA code)
  - Airline name
- Shows flight details and delay in minutes
- Delay data cleaned to handle NULLs and empty strings
- All queries handled with **parameterized SQL**
- Built with a **Menu interface** in the terminal
- Based on real-world structured flight data (SQLite)
- Extra: includes a basic HTML/CSS template (not used in logic)

---

## 🛠 Tech Stack

Python 3  
SQLite  
SQLAlchemy (Core)  
CLI interaction  
Raw SQL queries  
Optional: HTML/CSS static demo layout

---

## ▶️ How to Run

```bash
git clone https://github.com/your-username/Sky_SQL.git
cd Sky_SQL
python -m venv venv
venv\Scripts\activate    # On Windows
pip install -r requirements.txt
python main.py
```

Sky_SQL/
├── data/
│   ├── flights.sqlite3        # Flight dataset
│   ├── data.py                # Data access layer
│   └── main.py                # CLI application
├── _static/
│   ├── index_template.html    # Optional static template
│   └── style.css              # Basic CSS styling
├── requirements.txt
├── README.md
├── .gitignore