from swagger_server.models.auth_key import AuthKey
from swagger_server.models.user import User


import sqlalchemy as sqla
import bcrypt
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta

class DatabaseConn:

    def __init__(self):
        self.engine = sqla.create_engine('mysql://pybroker:mSWcwbTpuTv4Liwb@pma.tutorialfactory.org/pybroker', echo=True)
        #self.insert_user("demo@demo.de","test1234")
        #print(self.check_password( "demo@demo.de", "test123"))
        #print(self.check_auth_hash("6412048607212403114747023040737760377761651296630363127651933227449611792731"))


    def insert_user(self, user: User):
        auth_password = bcrypt.hashpw(User.password.encode('utf8'), bcrypt.gensalt())

        print(auth_password.decode('utf8'))

    def check_password(self, email: str, password: str) -> User:
        user = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("SELECT * FROM `users` WHERE `email` = :mail_address"), mail_address = email)
            for row in rs:
                hashAndSalt = row[4]
                userid = row[0]
                firstName = row[1]
                lastName = row[2]
                email = row [3]
                money_available = row [5]
                starting_capital = row[6]

                print(hashAndSalt)
                print(row)
        valid = bcrypt.checkpw(password.encode('utf8'), bytes(hashAndSalt, 'utf-8'))
        if (valid ):
            user =  User(userid,firstName,lastName,email,None,starting_capital,money_available)
        return user

    def generate_auth_hash(self, userid: int) -> AuthKey:
        if (userid is None):
            return None
        auth_key = random.getrandbits(256)
        expiry = self.util_format_datetime_for_expiry(2)
        with self.engine.connect() as con:
            con.execute(sqla.text("""INSERT INTO `user_authkey` (`userID`, `auth_key`, `expiry`) VALUES (:userid, :authkey, :expiry);"""), ( { "userid": userid, "authkey": auth_key , "expiry": expiry}))
        return AuthKey(userid,auth_key,expiry)

    def check_auth_hash(self, auth_key: str) ->AuthKey:
        auth_key = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("SELECT * FROM `user_authkey` WHERE `auth_key` = :authkey AND `expiry` <= 'now()' "),( { "authkey": auth_key }))
            for row in rs:
                userid = row[0]
                auth_key = row[1]
                expiry = row[2]
                auth_key = AuthKey(userid,auth_key,expiry)

        return auth_key
    def get_user_by_user_id(self, auth_key: str) ->User:
        user = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("SELECT * FROM `user_authkey` WHERE `auth_key` = :authkey AND `expiry` <= 'now()' "),( { "authkey": auth_key }))
            for row in rs:
                userid = row[0]
                auth_key = row[1]
                expiry = row[2]
                auth_key = AuthKey(userid,auth_key,expiry)

        return user

    def util_format_datetime_for_expiry(self, weeks: int) -> str:
        now = datetime.now()
        result = now + relativedelta(weeks=weeks)
        result = result.strftime('%Y-%m-%d %H:%M:%S')
        return result


    def get_all_stocks(self):
        """
        :desc: gets all WKNs in Database
        :return: Resultset
        """
        user = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("SELECT wkn FROM pybroker.tradable_values"))
        return rs
