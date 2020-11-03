from swagger_server.models.auth_key import AuthKey
from swagger_server.models.user import User
from swagger_server.models.stock_search_result import StockSearchResult
from swagger_server.models.transaction import Transaction
from swagger_server.models.transaction_prepare import TransactionPrepare
from swagger_server.models.stock_value import StockValue
from swagger_server.models.settings import Settings


from swagger_server.models.stock_description import StockDescription;

import sqlalchemy as sqla
import bcrypt
import random
import string
from datetime import datetime
from dateutil.relativedelta import relativedelta


class DatabaseConn:

    def __init__(self):
        self.engine = sqla.create_engine('mysql+pymysql://pybroker:mSWcwbTpuTv4Liwb@pma.tutorialfactory.org/pybroker',
                                         echo=True)
        # self.insert_user("demo@demo.de","test1234")
        # print(self.check_password( "demo@demo.de", "test123"))
        # print(self.check_auth_hash("6412048607212403114747023040737760377761651296630363127651933227449611792731"))

    def insert_user(self, user: User) -> bool:
        auth_password = bcrypt.hashpw(str(user.password).encode('utf8'), bcrypt.gensalt())
        returned = True
        try:
            with self.engine.connect() as con:
                con.execute(sqla.text(
                    """INSERT INTO `users` (`userID`, `first_name`, `last_name`, `email`, `auth_password`, `money_available`, `starting_capital`) VALUES (NULL, :first_name, :last_name, :email, :password, :money_available, :starting_capital);"""),
                    ({"first_name": user.first_name, "last_name": user.last_name, "email": user.email,
                      "password": auth_password.decode('utf8'), "money_available": user.money_available,
                      "starting_capital": user.starting_capital}))
        # print(auth_password.decode('utf8'))
        except:
            returned = False

        return returned

    def check_password(self, email: str, password: str) -> User:
        user = None
        valid = False
        hashAndSalt = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("SELECT * FROM `users` WHERE `email` = :mail_address"), mail_address=email)
            for row in rs:
                hashAndSalt = row[4]
                userid = row['userID']
                firstName = row[1]
                lastName = row[2]
                email = row[3]
                money_available = row[5]
                starting_capital = row[6]

                print(hashAndSalt)
                print(row)
        if (password is not None and hashAndSalt is not None):
            valid = bcrypt.checkpw(password.encode('utf8'), bytes(hashAndSalt, 'utf-8'))
        if (valid):
            user = User(userid, firstName, lastName, email, None, starting_capital, money_available)
        return user

    def generate_auth_hash(self, userid: int) -> AuthKey:
        if (userid is None):
            return None
        auth_key = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(128)))
        expiry = self.util_format_datetime_for_expiry(2)
        with self.engine.connect() as con:
            con.execute(sqla.text(
                """INSERT INTO `user_authkey` (`userID`, `auth_key`, `expiry`) VALUES (:userid, :authkey, :expiry);"""),
                ({"userid": userid, "authkey": auth_key, "expiry": expiry}))
        return AuthKey(userid, auth_key, expiry)

    def check_auth_hash(self, auth_key: str) -> AuthKey:
        auth_key_returned = None
        with self.engine.connect() as con:
            rs = con.execute(
                sqla.text("SELECT * FROM `user_authkey` WHERE `auth_key` = :authkey AND `expiry` >= now();"),
                ({"authkey": auth_key}))
            for row in rs:
                userid = row[0]
                auth_key = row[1]
                expiry = row[2]
                auth_key_returned = AuthKey(userid, auth_key, expiry)

        return auth_key_returned

    def get_user_by_auth_key(self, auth_key: str) -> User:
        user = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text(
                """SELECT * FROM `user_authkey` JOIN users on user_authkey.userID = users.userID WHERE `auth_key` = :authkey AND `expiry` >= now(); """),
                ({"authkey": auth_key}))
            for row in rs:
                user = User(row['userID'], row['first_name'], row['last_name'], row['email'], None,
                            row['starting_capital'], row['money_available'])

        return user

    def util_format_datetime_for_expiry(self, weeks: int) -> str:
        now = datetime.now()
        result = now + relativedelta(weeks=weeks)
        result = result.strftime('%Y-%m-%d %H:%M:%S')
        return result

    def get_stock_search_results(self) -> list:
        returnlist = []
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("SELECT `symbol`, `name` FROM `tradable_values`   "))
            for row in rs:
                returnlist.append(StockSearchResult(row['symbol'], row['name']))
        return returnlist

    def get_all_stocks(self) -> list:
        stockarray = []
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""SELECT * FROM `tradable_values`"""))
            for row in rs:
                stockarray.append(StockDescription(symbol=row['symbol'], stock_name=row['name'],
                                                   logo_url=row['logo_url']))

        return stockarray

        return rs


    def get_stock_by_symbol(self, symbol: str) -> StockDescription:
        returned = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""SELECT * FROM `tradable_values` WHERE `symbol` = :symbol"""),
                             ({"symbol": symbol}))
            for row in rs:
                returned = StockDescription(symbol=row['symbol'], stock_name=row['name'],
                                            logo_url=row['logo_url'])

        return returned

    def insert_transaction(self, transaction: TransactionPrepare, user: User) -> Transaction:
        returned= None
        with self.engine.connect() as con:
            con.execute(sqla.text("""INSERT INTO `transactions` (`transaction_id`, `user_id`, `symbol`, `course_id`, `amount`, `transaction_type`, `transaction_fee`) VALUES (NULL, :userid, :symbol, (SELECT id FROM `tradable_values_prices` WHERE `symbol` LIKE :symbol AND `timestamp` <= now() ORDER BY `timestamp` DESC LIMIT 1) , :amount, :buysell, :transaction_fee); """),
                             ({"symbol": transaction.symbol, "userid" : user.id, "amount" : transaction.amount, "buysell" : transaction.transaction_type, "transaction_fee" : 10}))
            rs = con.execute(sqla.text("""SELECT * FROM `transactions` JOIN tradable_values_prices ON transactions.course_id = tradable_values_prices.id WHERE `user_id` = :userid ORDER BY `transaction_id` DESC LIMIT 1  """), ({ "userid" : user.id }))
            for row in rs:
                returned = Transaction(id=row['transaction_id'], stock_value= StockValue(id=row['course_id'],symbol=row['symbol'],stock_price=row['market_value'], timestamp=row['timestamp']), amount = row['amount'], transaction_type= row['transaction_type'],transaction_fee= row['transaction_fee'])


        return returned

    def get_transactions_and_stock_by_user(self, user: User) -> dict:
        returned = []
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""SELECT * FROM `transactions` JOIN tradable_values_prices ON transactions.course_id = tradable_values_prices.id JOIN tradable_values ON transactions.symbol = tradable_values.symbol WHERE `user_id` = :userid """), ({ "userid" : user.id }))
            for row in rs:
                transaction = Transaction(id=row['transaction_id'], stock_value= StockValue(id=row['course_id'],symbol=row['symbol'],stock_price=row['market_value'], timestamp=row['timestamp']), amount = row['amount'], transaction_type= row['transaction_type'],transaction_fee= row['transaction_fee'])
                stocksearchresult = StockSearchResult(symbol=row['symbol'],stock_name=row['name'])
                returned.append((transaction,stocksearchresult))

        return returned

    def get_settings_by_user(self, user: User)-> Settings:
        transaction_fee = 10 # Default Value
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""SELECT * FROM `user_settings` WHERE `userid` = :userid """), ({ "userid" : user.id }))
            for row in rs:
                if row['user_setting'] == 'transaction_fee' : transaction_fee = row['value']
        returned = Settings(transaction_fee=transaction_fee)


        return returned

    def update_settings_by_user(self, user: User, settings: Settings): # Static for Transaction Fee, caution!!
        returned = True
        transaction_fee = settings.transaction_fee
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""UPDATE `user_settings` SET `value` = :newval WHERE (`user_settings`.`userid` = :userid) AND (`user_settings`.`user_setting` = :settingidentifier)   """), ({ "userid" : user.id , "newval": transaction_fee, "settingidentifier" : "transaction_fee"}))


        return returned


    def update_stock(self, stock_description: StockDescription):

        returned = False
        key = 0
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""UPDATE `tradable_values` SET `symbol` = :symbol, `name` = :name, `logo_url` = :logourl WHERE `tradable_values`.`symbol` = :symbol; """),({"symbol" : stock_description.symbol, "logourl" : stock_description.logo_url, "name" : stock_description.stock_name}) )
            returned = True
        return returned


    def insert_course(self, stock_value: StockValue):
        returned = False
        key = 0
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""INSERT INTO `tradable_values_prices` (`id`, `symbol`, `market_value`, `timestamp`) VALUES (NULL, :symbol, :marketprice, :datetime); """),({"symbol" : stock_value.symbol, "marketprice" : stock_value.stock_price, "datetime" : stock_value.timestamp}))
            returned = True
        return returned