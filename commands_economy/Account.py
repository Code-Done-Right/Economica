import asyncio
import asyncpg

async def OpenAccount(db_connection, user_id) -> bool:
    """
        OpenAccount checks if there is an existing account with the same ID.
        If there is one, creating a new account should not be allowed so therefore it returns False.
        Function Annotation:

        True: When there is no user in the db with the ID given.
        False: When there is an existing account.
    """

    USER_CONN = db_connection
    
    user = await USER_CONN.fetchrow('SELECT * FROM economica_bank WHERE user_id = $1', user_id) is not None
    if user == True:
        return True
    else:
        await USER_CONN.execute('''
            INSERT INTO economica_bank(user_id, wallet, bank) VALUES($1, $2, $3) ON CONFLICT DO NOTHING
            ''', user_id, 0, 0)

    return True

async def GetBankData(db_connection) -> None:
    """
        GetBankData returns the info of a specific database.
        Right now, I don't know whether this will be useful.
    """
    USER_CONN = db_connection