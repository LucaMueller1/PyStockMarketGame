#requirement: pip3 install psycopg2==2.7.5 (throws an error without specifying the version)

import psycopg2


#CONNECTION TO POSTGRES DATABASE
try:
    connection = psycopg2.connect(user = "uuhbagdexomt7wl1xyvi",
                                  password = "9Oom0Rul7outJ6JDwJSE",
                                  host = "bk9f1n0sei5c5bxablx7-postgresql.services.clever-cloud.com",
                                  port = "5432",
                                  database = "bk9f1n0sei5c5bxablx7")

    cursor = connection.cursor()

    #THIS IS WHERE AN INSERTION STATEMENT FOR DATABASE COULD BE SUCH AS:

    #postgres_insert_query = """INSERT INTO stockpurchase (stock_id, price) VALUES(BAYER, 200)"""
    #cursor.execute(postgres_insert_query)


    #Lines 17-23 are not essential for program (Displaying connection status and properties)
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

