"""
MISSING DOC STRING DOCUMENTATION
"""


def api_key_auth(apikey: str, required_scopes=None):
    if apikey == "lol123":
        return {'sub': 'admin'}

    # optional: raise exception for custom error response
    return None
