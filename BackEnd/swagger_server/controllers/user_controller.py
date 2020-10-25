import connexion
import six

from swagger_server.models.auth_key import AuthKey  # noqa: E501
from swagger_server.models.settings import Settings  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_prepare_login import UserPrepareLogin  # noqa: E501
from swagger_server import util


def create_user(user_param):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param user_param: Created user object
    :type user_param: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_param = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_user_settings(settings_param):  # noqa: E501
    """Create/set settings for logged in user

    Create/set the broker settings for the logged in user # noqa: E501

    :param settings_param: Created settings object
    :type settings_param: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        settings_param = Settings.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(user_id):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param user_id: The name that needs to be deleted
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_user_settings():  # noqa: E501
    """Get the settings of the logged in user

    Returns the settings of the logged in user # noqa: E501


    :rtype: Settings
    """
    return 'do some magic!'


def login_user(user_prepare_login_param):  # noqa: E501
    """Logs user into the system and returns auth key

     # noqa: E501

    :param user_prepare_login_param: Created user object
    :type user_prepare_login_param: dict | bytes

    :rtype: AuthKey
    """
    if connexion.request.is_json:
        user_prepare_login_param = UserPrepareLogin.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
