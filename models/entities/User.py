from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, username, password, fullname ="")-> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

#clave="scrypt:32768:8:1$uKhDhlryLo3SHOcl$16d3af57fdd9e0e1182f7240cbdb87c66e715ef3305cd2e2011540583c6fc819e75ed281f04af743778c1afa4dd02048dffd98ad6d5c750a66bf99f647f85d27"
#print(User.check_password(clave,'1234'))
