from swagger_server.services.db_service import DatabaseConn;
from swagger_server.models.auth_key import AuthKey

"""
MISSING DOC STRING DOCUMENTATION
"""

def api_key_auth(apikey: str, required_scopes=None):
    conn = DatabaseConn()
    auth_key = conn.check_auth_hash(apikey)

    if auth_key is None:
        print("Auth NOT accepted")
        return None
    else:
        print("Auth accepted")
        return {'sub': 'user'}

