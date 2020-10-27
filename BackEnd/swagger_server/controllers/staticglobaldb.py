from swagger_server.services.db_service import DatabaseConn


def init():
    global dbconn
    dbconn = DatabaseConn()
