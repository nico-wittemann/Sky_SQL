from sqlalchemy import create_engine, text

QUERY_FLIGHT_BY_ID = """
SELECT flights.*, airlines.airline, flights.ID as 
FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights 
JOIN airlines ON flights.airline = airlines.id 
WHERE flights.ID = :id"""

QUERY_FLIGHT_BY_DATE = """
SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY 
FROM flights 
JOIN airlines ON flights.airline = airlines.id 
WHERE flights.year = :year AND flights.month = :month AND flights.day = :day"""

QUERY_DELAYED_FLIGHT_BY_AIRPORT = """
SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY 
FROM flights 
JOIN airlines ON flights.airline = airlines.id 
WHERE flights.origin_airport = :airport 
AND DELAY > 0 
AND DELAY != ''
"""

QUERY_DELAYED_FLIGHT_BY_AIRLINE = """
SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY 
FROM flights 
JOIN airlines ON flights.airline = airlines.id 
WHERE airlines.airline = :airline 
AND DELAY > 0 
AND DELAY != ''"""

class FlightData:
    """
    The FlightData class is a Data Access Layer (DAL) object that provides an
    interface to the flight data in the SQLITE database. When the object is created,
    the class forms connection to the sqlite database file, which remains active
    until the object is destroyed.
    """

    def __init__(self, db_uri):
        """
        Initialize a new engine using the given database URI
        """
        self._engine = create_engine(db_uri)

    def _execute_query(self, query, params):
        """
        Execute an SQL query with the params provided in a dictionary,
        and returns a list of records (dictionary-like objects).
        If an exception was raised, print the error, and return an empty list.
        """
        with self._engine.connect() as connection:
            result = connection.execute(text(query), params)
            rows = result.fetchall()
            return rows

    def get_flight_by_id(self, flight_id):
        """
        Searches for flight details using flight ID.
        If the flight was found, returns a list with a single record.
        """
        params = {'id': flight_id}
        return self._execute_query(QUERY_FLIGHT_BY_ID, params)

    def get_flights_by_date(self, day, month, year):
        """
        Searches for flight details using flight date.
        If the flight was found, returns a list with a record.
        """
        params = {'day': day,
                  'month': month,
                  'year': year}
        return self._execute_query(QUERY_FLIGHT_BY_DATE, params)

    def get_delayed_flights_by_airport(self, airport):
        """
        Searches for details of delayed flights using the airport.
        If the flight was found, returns a list with a record.
        """
        params = {'airport': airport}
        return self._execute_query(QUERY_DELAYED_FLIGHT_BY_AIRPORT, params)

    def get_delayed_flights_by_airline(self, airline):
        """
        Searches for details of delayed flights using the airline.
        If the flight was found, returns a list with a record.
        """
        params = {'airline': airline}
        return self._execute_query(QUERY_DELAYED_FLIGHT_BY_AIRLINE, params)

    def __del__(self):
        """
        Closes the connection to the databse when the object is about to be destroyed
        """
        self._engine.dispose()
