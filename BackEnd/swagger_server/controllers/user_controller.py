import connexion
import six

from swagger_server.models.api_error import ApiError  # noqa: E501
from swagger_server.models.auth_key import AuthKey  # noqa: E501
from swagger_server.models.settings import Settings  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_prepare_login import UserPrepareLogin  # noqa: E501
from swagger_server import util
from swagger_server.controllers import staticglobaldb

"""
desc: User Controller that handles all requests concerning the user

author: Luca Mueller

date: 2020-10-14

mail: lucamueller32@gmail.com

version: 1.0

license: NONE
"""


def create_user(user_param):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param user_param: Created user object
    :type user_param: dict | bytes

    :rtype: None
    """
    insertion = False
    if connexion.request.is_json:
        user_param = User.from_dict(connexion.request.get_json())  # noqa: E501
        user_param.money_available = user_param.starting_capital
        insertion = staticglobaldb.dbconn.insert_user(user_param)

    if insertion:
        return 'OK', 200
    else:
        return ApiError(detail="Failed to create user", status=400, title="Bad Request", type="/user"), 400


def create_user_settings(settings_param):  # noqa: E501
    """Create/set settings for logged in user

    Create/set the broker settings for the logged in user # noqa: E501

    :param settings_param: Created settings object
    :type settings_param: dict | bytes

    :rtype: None
    """
    api_key = connexion.request.headers['api_key']
    if connexion.request.is_json:
        settings_param = Settings.from_dict(connexion.request.get_json())  # noqa: E501
        user = staticglobaldb.dbconn.get_user_by_auth_key(api_key)
        staticglobaldb.dbconn.update_settings_by_user(user, settings_param)
        return 'OK', 200


def delete_user(user_id):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param user_id: The name that needs to be deleted
    :type user_id: int

    :rtype: None
    """
    api_key = connexion.request.headers['api_key']
    user = staticglobaldb.dbconn.get_user_by_auth_key(api_key)
    staticglobaldb.dbconn.delete_user(user)
    return 'OK', 200


def get_user():  # noqa: E501
    """Get user from api_key

    This can only be done by the logged in user and will return a user object # noqa: E501


    :rtype: User
    """
    api_key = connexion.request.headers['api_key']
    print(api_key)
    if api_key is None:
        return ApiError(detail="No user authorized for given api_key", status=401, title="Unauthorized", type="/user"), 401
    user = staticglobaldb.dbconn.get_user_by_auth_key(api_key)

    return user


def get_user_settings():  # noqa: E501
    """Get the settings of the logged in user

    Returns the settings of the logged in user # noqa: E501


    :rtype: Settings
    """
    api_key = connexion.request.headers['api_key']
    user = staticglobaldb.dbconn.get_user_by_auth_key(api_key)
    settings = staticglobaldb.dbconn.get_settings_by_user(user)
    return settings


def login_user(user_prepare_login_param):  # noqa: E501
    """Logs user into the system and returns auth key

     # noqa: E501

    :param user_prepare_login_param: Created user object
    :type user_prepare_login_param: dict | bytes

    :rtype: AuthKey
    """
    if connexion.request.is_json:
        user_prepare_login_param = UserPrepareLogin.from_dict(connexion.request.get_json())  # noqa: E501

        conn = staticglobaldb.dbconn
        user = conn.check_password(user_prepare_login_param.email, user_prepare_login_param.password)
        if user is None:
            return ApiError(detail="User not found", status=404, title="Not Found", type="/user/login"), 404
        auth_key = conn.generate_auth_hash(user.id)

    return auth_key


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    api_key = connexion.request.headers['api_key']
    staticglobaldb.dbconn.delete_auth_key(api_key)
    return 'OK', 200
