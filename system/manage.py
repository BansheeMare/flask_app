import sqlite3


users_connection = sqlite3.connect('./archives/data/user_data.db')
users_cursor = users_connection.cursor()
#= sqlite3.connect('./data/user_data.db')
def get_user(user:str):
    users_cursor.execute(f"""
        SELECT *
        FROM access
        WHERE username = '{user}';
    """)
    fet = users_cursor.fetchall()
    if len(fet) > 0:
        users_cursor.execute(f"""
        SELECT *
        FROM account
        WHERE username = '{user}';
    """)
        account = users_cursor.fetchall()
        result = {
            'username':fet[0][0],
            'password':fet[0][1],
            'salt':fet[0][2],
            'balance':account[0][1],
            'level':account[0][2],
            'deposit':account[0][3]
            }

        return result

    return False

def insert_user(user:str, hash:str, salt:str):
    #try:
    users_cursor.execute(f"""
            INSERT INTO access (username, password, salt)
            VALUES ('{user}', '{hash}', '{salt}');
        """)
    users_connection.commit()
    users_cursor.execute(f"""
            INSERT INTO account (username, balance, level, deposit)
            VALUES ('{user}', 0, 0, 0);
        """)
    users_connection.commit()
    #    return True
    #except:
    #    return False   
def update_balance(user:str, new:int):
    users_cursor.execute(f"""
        UPDATE account
        SET balance = {new}
        WHERE username = '{user}';
    """)
    users_connection.commit()
    return True
    
def update_level(user:str, new:int):
    users_cursor.execute(f"""
        UPDATE account
        SET level = {new}
        WHERE username = '{user}';
    """)
    users_connection.commit()
    return True

def update_deposit(user:str, new:int):
    users_cursor.execute(f"""
        UPDATE account
        SET deposit = {new}
        WHERE username = '{user}';
    """)
    users_connection.commit()
    return True

def update_password(user:str, new:str):
    users_cursor.execute(f"""
        UPDATE access
        SET password = '{new}'
        WHERE username = '{user}';
    """)
    users_connection.commit()
    return True