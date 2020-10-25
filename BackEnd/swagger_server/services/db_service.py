import sqlalchemy as sqla
import bcrypt

class DatabaseConn:

    def __init__(self):
        self.engine = sqla.create_engine('mysql://pybroker:mSWcwbTpuTv4Liwb@pma.tutorialfactory.org/pybroker', echo=True)
        self.insert_user("demo@demo.de","test1234")
        self.check_password( "demo@demo.de", "test1234")


    def insert_user(self, username, password):
        auth_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        """with engine.connect() as con:
            data = ({"id": 1, "title": "The Hobbit", "primary_author": "Tolkien"},
                    {"id": 2, "title": "The Silmarillion", "primary_author": "Tolkien"},
                    )


            for line in data:
                con.execute(statement, **line)"""
        print(auth_password)

    def check_password(self, email: str, password: str) -> bool:
        data = ({"password": password})
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("SELECT * FROM `users` WHERE `email` = :password"), data)
            for row in rs:
                hashAndSalt = row[4]
                print(hashAndSalt)
                print(row)
        valid = bcrypt.checkpw(password.encode('utf8'), hashAndSalt)
        return valid

db= DatabaseConn()