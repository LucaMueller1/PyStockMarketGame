"""
desc: An authentication service that validates or invalidates a given API-Key
author: Luca Mueller
date: 2020-11-21
"""

from swagger_server.controllers import staticglobaldb
from swagger_server.models.auth_key import AuthKey


def api_key_auth(apikey: str, required_scopes=None):
    """Checks database for given API key and returns None if no valid Key is found

    :param apikey: API-Key provided by user
    :type apikey: str
    :param required_scopes: What authorization scope is needed
    :type required_scopes: object

    :rtype: Dict
    :test Correct: The provided apikey belongs to a logged-in user in the database and the method will return a dict. Incorrect: The provided API-Key does not exist in the database, thus the user will not be authorized and None is returned
    """
    auth_key = staticglobaldb.dbconn.check_auth_hash(apikey)

    if auth_key is None:
        print("Auth NOT accepted")
        return None
    else:
        print("Auth accepted")
        return {'sub': 'user'}

