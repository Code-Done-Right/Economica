import sqlite3

class Database ():
    """
    class `Database`
    
    Carries methods related to the SQL bot database.
    """

    def __init__():
        pass

    def initialise():
        """
        method `Database.initialise`

        Method of `Database`.
        Initialises the database when called in a file.
        """

        # Connection and cursor
        CONN = sqlite3.connect('bot.db')
        cursor = CONN.cursor()

        ECONOMY_TABLE = """CREATE TABLE IF NOT EXISTS Economy (
                user_id integer PRIMARY KEY,
                user_name text,
                wallet integer,
                bank_balance integer
            ); """

        MUTED_PEOPLE_TABLE = """CREATE TABLE IF NOT EXISTS Muted (
                user_id integer PRIMARY KEY,
                user_name text,
                duration integer
            ); """
        
        cursor.execute(ECONOMY_TABLE)
        cursor.execute(MUTED_PEOPLE_TABLE)

if __name__ == '__main__':
    Database.initialise()