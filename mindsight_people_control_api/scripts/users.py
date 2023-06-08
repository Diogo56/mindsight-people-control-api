from datetime import datetime

from mindsight_people_control_api.helpers.base_requests import (
    ApiPaginationResponse,
    BaseRequests,
)
from mindsight_people_control_api.settings import (
    API_ENDPOINT_USERS,
    PAGE_SIZE,
    datetime_format,
)


class Users:
    base_requests = BaseRequests()

    def __init__(self) -> None:
        self.base_requests.BASE_PATH = API_ENDPOINT_USERS
        self.PAGE_SIZE = PAGE_SIZE

    def get_list_users(
        self,
        search: str = None,
    ) -> ApiPaginationResponse:
        """Get areas data
        Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Users/operation/listUsers

        Args:
            search: A search term.
        """

        path = ""
        parameters = {
            "search": search,
            "page_size": self.PAGE_SIZE,
        }
        return self.base_requests.get(path=path, parameters=parameters)

    def get_retrieve_user(
        self,
        id: int,
        search: str = None,
    ) -> dict:
        """Get retrieve user
        Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Users/operation/retrieveUser

        Args:
            id (int, Mandatory): Id of user to retrieve
            search (str, Optional): search
        """
        path = f"/{id}"

        parameters = {
            "search": search,
        }
        return self.base_requests.get(
            path=path,
            parameters=parameters,
        )

    def post_create_user(
        self,
        username: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        is_superuser: bool = False,
        is_staff: bool = False,
        is_active: bool = False,
        last_login: datetime = None,
        date_joined: datetime = datetime.now(),
    ):
        """Create new area
        Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Users/operation/createUser

        Args:
            username (str, Mandatory): Username with 254 characters or fewer. Letters, digits and @/./+/-/_ only
            email (str, Optional): User email with 254 characters or fewer
            first_name (str, Optional): User first name with 100 characters or fewer
            last_name (str, Optional): User last name with 150 characters or fewer
            is_superuser (bool, Optional): Super user permission
            is_staff (bool, Optional): Access to admin site
            is_active (bool, Optional): Access to front site
            last_login (datetime, Optional): Datetime of last login
            date_joined (datetime, Optional): Datetime of user joined
        """
        path = ""
        data = {
            "username": username,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "is_superuser": is_superuser,
            "is_staff": is_staff,
            "is_active": is_active,
            "last_login": last_login.strftime(datetime_format) if last_login else None,
            "date_joined": date_joined.strftime(datetime_format)
            if date_joined
            else None,
        }

        return self.base_requests.post(path=path, json=data)

    def patch_update_user(
        self,
        id: int,
        username: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        is_superuser: bool = False,
        is_staff: bool = False,
        is_active: bool = False,
        last_login: datetime = None,
        date_joined: datetime = None,
    ) -> dict:
        """Edit partial user register
        Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Users/operation/partialUpdateUser

        Args:
            id (int, Mandatory): Area id
            username (str, Mandatory): Username with 254 characters or fewer. Letters, digits and @/./+/-/_ only
            email (str, Optional): User email with 254 characters or fewer
            first_name (str, Optional): User first name with 100 characters or fewer
            last_name (str, Optional): User last name with 150 characters or fewer
            is_superuser (bool, Optional): Super user permission
            is_staff (bool, Optional): Access to admin site
            is_active (bool, Optional): Access to front site
            last_login (datetime, Optional): Datetime of last login
            date_joined (datetime, Optional): Datetime of user joined
        """
        path = f"/{id}"
        data = {
            "username": username,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "is_superuser": is_superuser,
            "is_staff": is_staff,
            "is_active": is_active,
            "last_login": last_login.strftime(datetime_format) if last_login else None,
            "date_joined": date_joined.strftime(datetime_format)
            if date_joined
            else None,
        }
        return self.base_requests.patch(path=path, data=data)

    def put_full_update_user(
        self,
        id: int,
        username: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        is_superuser: bool = False,
        is_staff: bool = False,
        is_active: bool = False,
        last_login: datetime = None,
        date_joined: datetime = None,
    ) -> dict:
        """Edit full user register
        Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Users/operation/updateUser

        Args:
            id (int, Mandatory): Area id
            username (str, Mandatory): Username with 254 characters or fewer. Letters, digits and @/./+/-/_ only
            email (str, Optional): User email with 254 characters or fewer
            first_name (str, Optional): User first name with 100 characters or fewer
            last_name (str, Optional): User last name with 150 characters or fewer
            is_superuser (bool, Optional): Super user permission
            is_staff (bool, Optional): Access to admin site
            is_active (bool, Optional): Access to front site
            last_login (datetime, Optional): Datetime of last login
            date_joined (datetime, Optional): Datetime of user joined
        """
        path = f"/{id}"
        data = {
            "username": username,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "is_superuser": is_superuser,
            "is_staff": is_staff,
            "is_active": is_active,
            "last_login": last_login.strftime(datetime_format) if last_login else None,
            "date_joined": date_joined.strftime(datetime_format)
            if date_joined
            else None,
        }
        return self.base_requests.put(path=path, data=data)

    def delete_destroy_user(self, id: int, search: str = None):
        path = f"/{id}"

        parameters = {
            "search": search,
        }
        return self.base_requests.delete(path=path, parameters=parameters)