from .entities.User import User
from database.data_psql import get_connection

class ModelUser():

    @classmethod
    def login(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query =f"SELECT id, user_admin, password, fullname FROM administradores WHERE user_admin ='{user.username}'"
                cursor.execute(query)
                row = cursor.fetchone()
                if row != None:
                    user = User(row[0], row[1], User.check_password(row[2],user.password),row[3])
                    return user
                else:
                    return None
            connection.close()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = "SELECT id, user_admin, fullname FROM administradores WHERE id = {}".format(id)
                cursor.execute(query)
                row = cursor.fetchone()
                if row != None:
                    return User(row[0], row[1], None, row[2])
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)



#print(ModelUser.login('gomezedj@gmail.com'))