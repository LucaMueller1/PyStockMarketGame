import connexion
import six

from swagger_server.models.auth_key import AuthKey  # noqa: E501
from swagger_server.models.login_user import LoginUser  # noqa: E501
from swagger_server.models.settings import Settings  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_user(User):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param User: Created user object
    :type User: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        User = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_user_settings(Settings):  # noqa: E501
    """Create/set settings for logged in user

    Create/set the broker settings for the logged in user # noqa: E501

    :param Settings: Created settings object
    :type Settings: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Settings = Settings.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(userid):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param userid: The name that needs to be deleted
    :type userid: int

    :rtype: None
    """
    return 'do some magic!'


def get_user_settings():  # noqa: E501
    """Get the settings of the logged in user

    Returns the settings of the logged in user # noqa: E501


    :rtype: Settings
    """
    return 'do some magic!'


def login_user(LoginUser):  # noqa: E501
    """Logs user into the system and returns auth key

     # noqa: E501

    :param LoginUser: Created user object
    :type LoginUser: dict | bytes

    :rtype: AuthKey
    """
    if connexion.request.is_json:
        LoginUser = LoginUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
