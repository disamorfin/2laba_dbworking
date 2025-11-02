from main import createConnection, getResult

connection = createConnection()
cursor = connection.cursor()

def createStudent():
    user_group_id = input("user_group_id: ")
    username = input("username: ")
    password = input("password: ")
    firstname = input("firstname: ")
    lastname = input("lastname: ")
    email = input("email: ")
    code = input("code: ")
    ip = input("ip: ")
    status = input("status (0/1): ")
        
    try:
            insert_query = """
            INSERT INTO user 
            (user_group_id, username, password, firstname, lastname, email, code, ip, status, date_added) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """

            values = (user_group_id, username, password, firstname, lastname, email, code, ip, status)

            cursor.execute(insert_query, values)
            connection.commit()
    finally:
            cursor.close()
            connection.close()

getResult(connection)