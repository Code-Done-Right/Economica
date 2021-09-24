async def OpenAccount(db_connection, username):
    USER_CONN = db_connection
    
    user = await USER_CONN.fetchrow('SELECT * FROM users WHERE username = $1', username)
    print(user)
    

async def GetBankData(db_connection):
    pass