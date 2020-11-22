from swagger_server.services.db_service import DatabaseConn

"""

    desc: Is used to serve a static "DatabaseConn" Object that can be accessed statically.

    author: Daniel Ebert

    date: 2020-11-01

"""

def init():
    global dbconn
    dbconn = DatabaseConn()
