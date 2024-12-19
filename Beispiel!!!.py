from sqlalchemy import text, create_engine


# Ask the user for search term
year_input = input("Enter a search year for the books catalog: ")

# Create params dict
params = {"year": year_input}

# Create an engine that connects to a SQLite database file named "example.sqlite3"
engine = create_engine('sqlite:///data/textbook.sqlite3')   # Make sure to move the data into the data directory!


with engine.connect() as connection:

  query = 'SELECT * FROM books WHERE publication_year = :year'
  results = connection.execute(text(query), params)
  rows = results.fetchall()

  # Print num of results
  print(f"Returned {len(rows)} results")

  # Print results
  for row in rows:
    print(row.title)