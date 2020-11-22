from swagger_server.models.auth_key import AuthKey
from swagger_server.models.user import User
from swagger_server.models.stock_search_result import StockSearchResult
from swagger_server.models.transaction import Transaction
from swagger_server.models.transaction_prepare import TransactionPrepare
from swagger_server.models.stock_value import StockValue
from swagger_server.models.settings import Settings

from swagger_server.models.stock_description import StockDescription

import sqlalchemy as sqla
import bcrypt
import random
import string
from datetime import datetime
from dateutil.relativedelta import relativedelta


class DatabaseConn:
    """

        desc: Handles the Database Connection as well as all Database related functions

        author: Daniel Ebert

        date: 2020-11-09

    """

    def __init__(self):
        """

            desc: database init function, initializes Database Engine

            param: (str) databaseAddress, (str) databaseuser, (str) databasePassword, (str) databaseName


        """
        self.engine = sqla.create_engine('mysql+pymysql://username:password@hostname/database',
                                         echo=False, pool_size=5, pool_recycle=3600)

    def insert_user(self, user: User) -> bool:
        """

            desc: insert User into Database Function. Called after registering

            param: (User) user

            test: Correct: If a valid user object is passed with all values tha need to be inserted, the method returns true. Incorrect: If an attribute has the wrong type inside the class, e.g. Money_available is passed as a String, the method returns false

        """
        auth_password = bcrypt.hashpw(str(user.password).encode('utf8'), bcrypt.gensalt())
        returned = True
        try:
            with self.engine.connect() as con:
                con.execute(sqla.text(
                    """INSERT INTO `users` (`userID`, `first_name`, `last_name`, `email`, `auth_password`, `money_available`, `starting_capital`) VALUES (NULL, :first_name, :last_name, :email, :password, :money_available, :starting_capital);"""),
                    ({"first_name": user.first_name, "last_name": user.last_name, "email": user.email,
                      "password": auth_password.decode('utf8'), "money_available": user.money_available,
                      "starting_capital": user.starting_capital}))
                con.execute(sqla.text(
                    """INSERT INTO `user_settings` (`id`, `userid`, `user_setting`, `value`) VALUES (NULL, (SELECT last_insert_id()), :setting_name, :setting_val);"""),
                    ({"setting_name": "transaction_fee", "setting_val": "10"}))
        # print(auth_password.decode('utf8'))
        except:
            returned = False

        return returned

    def delete_auth_key(self, authkey: str) -> bool:
        """

            desc: Function to remove the auth key out of the database, for example called after the log out of a user

            param: (str) authKey,

            test: Correct: If a valid authkey is passed to the function, it will get removed from the database. Incorrect: The function does return false if a SQL Error occurs.

        """
        returned = True
        try:
            with self.engine.connect() as con:
                con.execute(sqla.text(
                    """DELETE FROM `user_authkey` WHERE `user_authkey`.`auth_key` = :authkey ;"""),
                    ({"authkey": authkey}))
        except:
            returned = False

        return returned

    def delete_user(self, user: User) -> bool:
        """

            desc: Function to remove the user out of the database, called when the user wants to delete its account

            param: (User) The user object, all objects apart from the ID are nullable

            test: Correct: If a valid user with the user.id variable set is passed to the function, it will get removed from the database. The function does return true if no SQL Error occurs. Incorrect: The userid is passed as a String -> is passed with the wrong type

        """
        returned = True
        try:
            with self.engine.connect() as con:
                con.execute(sqla.text(
                    """DELETE FROM `users` WHERE `users`.`userID` = :userid"""),
                    ({"userid": user.id}))
        except:
            returned = False

        return returned

    def check_password(self, email: str, password: str) -> User:
        """

            desc: Function to validate a users login credentials

            param: (str) email, (str) password

            test: Correct: If a valid email/password combination is passed the function will return a User object. Otherwise it will return None

        """
        user = None
        valid = False
        hashAndSalt = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""SELECT * FROM `users` WHERE `email` = :mail_address"""), mail_address=email)
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
        if password is not None and hashAndSalt is not None:
            valid = bcrypt.checkpw(password.encode('utf8'), bytes(hashAndSalt, 'utf-8'))
        if valid:
            user = User(userid, firstName, lastName, email, None, starting_capital, money_available)
        return user

    def generate_auth_hash(self, userid: int) -> AuthKey:
        """

            desc: Function to generate an AuthHash/ SessionKey

            param: (int) userid

            test: Correct: If a valid userid is passed the inserted AuthKey obj is returned

        """
        if userid is None:
            return None
        auth_key = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(128)))
        expiry = self.util_format_datetime_for_expiry(2)
        with self.engine.connect() as con:
            con.execute(sqla.text(
                """INSERT INTO `user_authkey` (`userID`, `auth_key`, `expiry`) VALUES (:userid, :authkey, :expiry);"""),
                ({"userid": userid, "authkey": auth_key, "expiry": expiry}))
        return AuthKey(userid, auth_key, expiry)

    def check_auth_hash(self, auth_key: str) -> AuthKey:
        """

            desc: Function to validate an AuthHash/ SessionKey

            param: (str) authkey

            test: Correct: IF a valid authHash is passed as a String, the method will return an AuthKey object, filled with the userid the key belongs to and the expiry date. Otherwise, it will return None.

        """
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
        """

            desc: Function to get a User object based on the auth key

            param: (str) auth_key

            test: Correct: If a valid authkey belonging to a user is passed, the method returns an object of the type User. Otherwise it will return None

        """
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
        """

            desc: Helper function to generate an Datetime String two weeks in the future from the actual datetime

            param: (int) weeks

            test: Correct: If a calculateable number is passed , the method will return a string with the formatted (datetime now + the passed amount of weeks). If weeks is passed with a number too high for the datetime library to calculate it, it will throw an error

        """
        now = datetime.now()
        result = now + relativedelta(weeks=weeks)
        result = result.strftime('%Y-%m-%d %H:%M:%S')
        return result

    def get_stock_search_results(self) -> list:
        """

            desc: Function to return all stocks with their symbol and their name only (Using the object StockSearchResult) from the database for the frontend search box.

            param: None

            test: Since the function does not take parameters, it will always return a list of StockSearchResult or throw an sqlError.

        """
        returnlist = []
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("SELECT `symbol`, `name` FROM `tradable_values`   "))
            for row in rs:
                returnlist.append(StockSearchResult(row['symbol'], row['name']))
        return returnlist

    def get_all_stocks(self) -> list:
        """

            desc: Function to return a list of StockDescription objects with all stocks in the database.

            param: None

            test: The function should always return a list of StockDescription or throw an sqlerror

        """
        stockarray = []
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""SELECT * FROM `tradable_values`"""))
            con.inser
            for row in rs:
                stockarray.append(StockDescription(symbol=row['symbol'], stock_name=row['name'],
                                                   logo_url=row['logo_url']))

        return stockarray

        return rs

    def get_stock_by_symbol(self, symbol: str) -> StockDescription:
        """

            desc: Function to return a StockDescription object of the stock found in the database with a specific symbol given.

            param: (str) symbol

            test: If a symbol that's present in the database is passed, a StockDescription object is returned. If the symbol is not found in the database, None will be returned

        """
        returned = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""SELECT * FROM `tradable_values` WHERE `symbol` = :symbol"""),
                             ({"symbol": symbol}))
            for row in rs:
                returned = StockDescription(symbol=row['symbol'], stock_name=row['name'],
                                            logo_url=row['logo_url'])

        return returned

    def insert_transaction(self, transaction: TransactionPrepare, user: User) -> Transaction:
        """

            desc: Function to insert a transaction into the database

            param: (TransactionPrepare) transaction, (User) user

            test: If all values in the TransactionPrepare object are set and the user object has a valid userid the function does insert the transaction into the database. Incorrect: The stock has not yet a course inserted and therefore the INSERT method will fail. The inserted Transaction is SELECTED and then returned.

        """
        returned = None
        with self.engine.connect() as con:
            con.execute(sqla.text(
                """INSERT INTO `transactions` (`transaction_id`, `user_id`, `symbol`, `course_id`, `amount`, `transaction_type`, `transaction_fee`) VALUES (NULL, :userid, :symbol, (SELECT id FROM `tradable_values_prices` WHERE `symbol` LIKE :symbol AND `timestamp` <= now() ORDER BY `timestamp` DESC LIMIT 1) , :amount, :buysell, (SELECT user_settings.value FROM `user_settings` WHERE user_settings.userid = :userid AND user_settings.user_setting = 'transaction_fee')); """),
                ({"symbol": transaction.symbol, "userid": user.id, "amount": transaction.amount,
                  "buysell": transaction.transaction_type}))
            rs = con.execute(sqla.text(
                """SELECT * FROM `transactions` JOIN tradable_values_prices ON transactions.course_id = tradable_values_prices.id WHERE `user_id` = :userid ORDER BY `transaction_id` DESC LIMIT 1  """),
                ({"userid": user.id}))
            for row in rs:
                returned = Transaction(id=row['transaction_id'],
                                       stock_value=StockValue(id=row['course_id'], symbol=row['symbol'],
                                                              stock_price=row['market_value'],
                                                              timestamp=row['timestamp']), amount=row['amount'],
                                       transaction_type=row['transaction_type'], transaction_fee=row['transaction_fee'])

        return returned

    def get_transactions_and_stock_by_user(self, user: User) -> dict:
        """

            desc: Get all transactions from a specific user

            param: (User) user

            test: If a Userid present in the database is passed, the method will either return an empty list if no transactions are present yet or a tupel of objects of the type Transaction, paired with an object of the type StockDescription. Incorrect: Passed user object has no or wrong ID.

        """
        returned = []
        with self.engine.connect() as con:
            rs = con.execute(sqla.text(
                """SELECT * FROM `transactions` JOIN tradable_values_prices ON transactions.course_id = tradable_values_prices.id JOIN tradable_values ON transactions.symbol = tradable_values.symbol WHERE `user_id` = :userid """),
                ({"userid": user.id}))
            for row in rs:
                transaction = Transaction(id=row['transaction_id'],
                                          stock_value=StockValue(id=row['course_id'], symbol=row['symbol'],
                                                                 stock_price=row['market_value'],
                                                                 timestamp=row['timestamp']), amount=row['amount'],
                                          transaction_type=row['transaction_type'],
                                          transaction_fee=row['transaction_fee'])
                stocksearchresult = StockDescription(symbol=row['symbol'], stock_name=row['name'],
                                                     logo_url=row['logo_url'])
                returned.append((transaction, stocksearchresult))

        return returned

    def get_settings_by_user(self, user: User) -> Settings:
        """

            desc: Get all Settings from a specified user

            param: (User) user

            test: If a user object is passed with a valid id, a Settings object is returned consisting of the users settings. Incorrect: The users settings are not found in the database

        """
        transaction_fee = 10  # Default Value
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""SELECT * FROM `user_settings` WHERE `userid` = :userid """),
                             ({"userid": user.id}))
            for row in rs:
                if row['user_setting'] == 'transaction_fee': transaction_fee = float(row['value'])
        returned = Settings(transaction_fee=transaction_fee)

        return returned

    def update_settings_by_user(self, user: User, settings: Settings):
        """

            desc: Update the settings for a specific user

            param: (User) user, (Settings) settings

            test: If the user object has a valid id in the database and the user settings were properly set, the method will return True

        """
        returned = True
        transaction_fee = settings.transaction_fee
        with self.engine.connect() as con:
            rs = con.execute(sqla.text(
                """UPDATE `user_settings` SET `value` = :newval WHERE (`user_settings`.`userid` = :userid) AND (`user_settings`.`user_setting` = :settingidentifier)   """),
                ({"userid": user.id, "newval": transaction_fee, "settingidentifier": "transaction_fee"}))

        return returned

    def update_stock(self, stock_description: StockDescription):
        """

            desc: Update the settings for a specific user

            param: (User) user, (Settings) settings

            test: If the user object has a valid id in the database and the user settings were properly set, the method will return True

        """
        returned = False
        key = 0
        with self.engine.connect() as con:
            rs = con.execute(sqla.text(
                """UPDATE `tradable_values` SET `symbol` = :symbol, `name` = :name, `logo_url` = :logourl WHERE `tradable_values`.`symbol` = :symbol; """),
                ({"symbol": stock_description.symbol, "logourl": stock_description.logo_url,
                  "name": stock_description.stock_name}))
            returned = True
        return returned

    def insert_course(self, stock_value: StockValue):
        """

            desc: Insert course into the database

            param: (StockValue) stock_value

            test: If all attributes in the StockValue object are properly set, the course gets inserted into the database. If for example the date is missing, an error is thrown.

        """
        returned = False
        key = 0
        if (self.get_stock_price_from_date(stock_value.symbol, stock_value.timestamp)) is not None:
            return True
        with self.engine.connect() as con:
            rs = con.execute(sqla.text(
                """INSERT INTO `tradable_values_prices` (`id`, `symbol`, `market_value`, `timestamp`) VALUES (NULL, :symbol, :marketprice, :datetime); """),
                ({"symbol": stock_value.symbol, "marketprice": stock_value.stock_price,
                  "datetime": stock_value.timestamp}))
            returned = True
        return returned

    def get_stock_price_from_today(self, stock_symbol: str) -> StockValue:
        """

            desc: Get the stock price from today by a stock symbol

            param: (str) stock_symbol

            test: If a stock_price is available for the given symbol and the date of today, a StockValue object is returned. Otherwise None.

        """
        # return StockValue Object
        returned = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text(
                """SELECT * FROM `tradable_values_prices` WHERE `symbol` LIKE :symbol AND `timestamp` = CURRENT_DATE() ORDER BY `timestamp` DESC LIMIT 1"""),
                ({"symbol": stock_symbol}))
            for row in rs:
                returned = StockValue(id=row['id'], symbol=row['symbol'], stock_price=row['market_value'],
                                      timestamp=row['timestamp'])
        return returned

    def get_stock_price_from_date(self, stock_symbol: str, history_date: datetime) -> StockValue:
        """

            desc: Get the stock price from a specific date by a stock symbol

            param: (str) stock_symbol

            test: If a stock_price is available for the given symbol and the given date, a StockValue object is returned. Otherwise None.

        """
        returned = None
        with self.engine.connect() as con:
            rs = con.execute(sqla.text(
                """SELECT * FROM `tradable_values_prices` WHERE `symbol` LIKE :symbol AND `timestamp` = :history_date ORDER BY `timestamp` DESC LIMIT 1"""),
                ({"symbol": stock_symbol, "history_date": history_date}))
            for row in rs:
                returned = StockValue(id=row['id'], symbol=row['symbol'], stock_price=row['market_value'],
                                      timestamp=row['timestamp'])
        return returned

    def get_latest_stock_price(self, stock_symbol: str) -> StockValue:
        """

            desc: Get the latest stock price available

            param: (str) stock_symbol

            test: If any stock_price is available for the passed symbol, the latest value embedded in a StockValue object is returned. Otherwise None.

        """
        with self.engine.connect() as con:
            rs = con.execute(sqla.text(
                """SELECT * FROM `tradable_values_prices` WHERE `symbol` LIKE :symbol ORDER BY `timestamp` DESC LIMIT 1"""),
                ({"symbol": stock_symbol}))
            for row in rs:
                returned = StockValue(id=row['id'], symbol=row['symbol'], stock_price=row['market_value'],
                                      timestamp=row['timestamp'])
        return returned

    def update_user(self, user: User) -> bool:
        """

             desc: Update all attributes for a user in the database

             param: (User) user

             test: If all attirbutes have the right types, the method will return True. If money_available is passed as a string, it will return False.

         """
        returned = False
        with self.engine.connect() as con:
            rs = con.execute(sqla.text(
                """UPDATE `users` SET `first_name` = :first_name, `last_name` = :last_name, `email` = :email, `money_available` = :money_available, `starting_capital` = :starting_capital WHERE `users`.`userID` = :userid;  """),
                ({"first_name": user.first_name, "userid": user.id, "last_name": user.last_name,
                  "email": user.email, "money_available": user.money_available,
                  "starting_capital": user.starting_capital}))
            returned = True
        return returned

    def get_all_users(self) -> list:
        """

             desc: Get a list of all users in the database

             param: None

             test: Correct: Should always return a list of users and if the database is empty it will return an empty list.
         """
        users = []
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""SELECT * FROM `users` """))
            for row in rs:
                users.append(User(row['userID'], row['first_name'], row['last_name'], row['email'], None,
                                  row['starting_capital'], row['money_available']))

        return users

    def get_all_stocks_distinct_in_transactions(self) -> list:
        """

             desc: Get a distinct list symbols in the transaction table

             param: None

             test: Correct: Should always return a list of symbols and if the transactions table is empty an empty list.
         """
        symbols = []
        with self.engine.connect() as con:
            rs = con.execute(sqla.text("""SELECT DISTINCT symbol FROM `transactions` """))
            for row in rs:
                symbols.append(row['symbol']);

        return symbols