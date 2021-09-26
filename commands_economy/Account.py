import asyncio
import asyncpg

async def OpenAccount(db_connection, user_id, username, discriminator) -> bool:
    """
        OpenAccount checks if there is an existing account with the same name and discriminator.
        If there is one, creating a new account should not be allowed so therefore it returns False.
        Function Annotation:

        True: When there is no user in the db with the username and discriminator given.
        False: When there is an existing account.
    """

    USER_CONN = db_connection
    
    user = await USER_CONN.fetchrow('SELECT * FROM users WHERE username = $1, discriminator = $2', username, discriminator) is not None
    if user == True:
        return False
    else:
        await USER_CONN.execute('''
            INSERT INTO economicausers(user_id, username, discriminator, wallet, bank) VALUES($1, $2, $3, $4, $5)
            ''', user_id, username, discriminator, 0, 0)

    return True

async def GetBankData(db_connection):
    """
        GetBankData returns the info of a specific database.
        Right now, I don't know whether to keep this.
    """
    USER_CONN = db_connection

    