from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserGet(BaseCase):
    def test_get_user_details_not_auth_username(self):
        response = MyRequests.universal_method("GET", "/user/2")
        Assertions.assert_json_has_key(response, "username")

    def test_get_user_details_not_auth_first_name(self):
        response = MyRequests.universal_method("GET", "/user/2")
        Assertions.assert_json_not_has_key(response, "firstName")

    def test_get_user_details_not_auth_last_name(self):
        response = MyRequests.universal_method("GET", "/user/2")
        Assertions.assert_json_not_has_key(response, "lastName")

    def test_get_user_details_not_auth_email(self):
        response = MyRequests.universal_method("GET", "/user/2")
        Assertions.assert_json_not_has_key(response, "email")

    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.universal_method("POST", "/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.universal_method(method="GET", url=f"/user/{user_id_from_auth_method}",
                                                headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        expected_fields = ["username", "firstName", "lastName", "email"]
        Assertions.assert_json_has_keys(response2, expected_fields)
