import sqlalchemy as sqla
import bcrypt
import auth_key

class DatabaseConn:

    def __init__(self):
        self.engine = sqla.create_engine('mysql://pybroker:mSWcwbTpuTv4Liwb@pma.tutorialfactory.org/pybroker', echo=True)
        self.insert_user("demo@demo.de","test1234")
        print(self.check_password( "demo@demo.de", "test1234"))


    def insert_user(self, username, password):
        auth_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        print(auth_password.decode('utf8'))

    def check_password(self, email: str, password: str) -> bool:
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("SELECT * FROM `users` WHERE `email` = :mail_address"), mail_address = email)
            for row in rs:
                hashAndSalt = row[4]
                print(hashAndSalt)
                print(row)
        valid = bcrypt.checkpw(password.encode('utf8'), bytes(hashAndSalt, 'utf-8'))
        return valid
    def generate_auth_hash(self, userid: int)-> :
db= DatabaseConn()