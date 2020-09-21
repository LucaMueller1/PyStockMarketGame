#requirement: pip3 install psycopg2==2.7.5 (throws an error without specifying the version), pip3 install bs4 (BeautifulSoupe

import psycopg2
import uuid
import requests
from bs4 import BeautifulSoup

#CONNECTION TO POSTGRES DATABASE
try:
    connection = psycopg2.connect(user = "uuhbagdexomt7wl1xyvi",
                                  password = "9Oom0Rul7outJ6JDwJSE",
                                  host = "bk9f1n0sei5c5bxablx7-postgresql.services.clever-cloud.com",
                                  port = "5432",
                                  database = "bk9f1n0sei5c5bxablx7")

    cursor = connection.cursor()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)


def initialise_user(username, cash):
    #Add username to user table
    postgres_insert_query = """INSERT INTO public.user (user_name, user_id) VALUES(%s, %s)"""
    user_id = str(uuid.uuid4())
    record_to_insert = (username, user_id)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")
    __addPortfolioDB(cash, user_id)

def __addPortfolioDB(cash, user_id):
    postgres_insert_query = """INSERT INTO public.portfolio (portfolio_id, cash, user_id ) VALUES(%s, %s, %s)"""
    portfolio_id = str(uuid.uuid4())
    #securities_value default = 0 --> no need to specify in Code
    record_to_insert = (portfolio_id, cash, user_id)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")


    
def stock_purchase(user_name2, stock_ticker, stock_quantity):
    stock_buyin = float(__real_time_stockprice(stock_ticker))
    #Get User ID from username
    insertion_name = (str(user_name2), )
    cursor.execute("""SELECT user_id from public.user WHERE user_name= %s """, (insertion_name))
    user_id = cursor.fetchone()

    #Get portfolio ID from User ID
    cursor.execute("""SELECT portfolio_id from public.portfolio WHERE user_id= %s""", (user_id))
    portfolio_id = cursor.fetchone()


    #Filling out a row in stocks_purchase in the following order: purchase_id, stock_ticker, stock_quantity, stock_buyin
    postgres_insert_query = """INSERT INTO public.stocks_purchases (purchase_id, stock_ticker, stock_quantity, stock_buyin, portfolio_id ) VALUES(%s, %s, %s, %s, %s)"""
    purchase_id = str(uuid.uuid4())
    record_to_insert = (purchase_id, stock_ticker, stock_quantity, stock_buyin, portfolio_id)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

    update_portfolio_table(user_name2)


def update_portfolio_table(user_name):
    # Get User ID from username
    insertion_name = (str(user_name),)
    cursor.execute("""SELECT user_id from public.user WHERE user_name= %s """, (insertion_name))
    user_id = cursor.fetchone()

    #Get portfolio ID from User ID
    cursor.execute("""SELECT portfolio_id from public.portfolio WHERE user_id= %s""", (user_id))
    portfolio_id = cursor.fetchone()


    cursor.execute("""SELECT * FROM public.stocks_purchases WHERE portfolio_id= %s""", (portfolio_id))
    data = cursor.fetchall()
    print(len(data))
    i = 0
    total_portfolio_value = 0
    while i < len(data):
        stock_code = data[i][0]
        current_price_of_entry = __real_time_stockprice(stock_code)
        total_value_of_stock = current_price_of_entry * data[i][1]
        total_portfolio_value = float(total_portfolio_value) + float(total_value_of_stock)
        i = i + 1

    print(total_portfolio_value)

    #Insert that value into the database
    cursor.execute("""UPDATE public.portfolio SET securities_value = %s  WHERE portfolio_id = %s""", (total_portfolio_value, portfolio_id))
    connection.commit()


def __real_time_stockprice(stock_code):
    url = ("https://finance.yahoo.com/quote/" + stock_code + "/")
    r = requests.get(url)
    web_content = BeautifulSoup(r.text, "lxml")
    web_content = web_content.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px)")
    web_content = web_content.find("span").text
    return web_content


"""
How to use:
1. Create user (automatically creates a portfolio) --> parameters: user_name, cash
2. buy a stock --> parameters: user_name, stock ticker, stock_quantity
"""
update_portfolio_table("Luca")

cursor.close()
connection.close()
print("PostgreSQL connection is closed")

