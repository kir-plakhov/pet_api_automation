from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    def test_create_user_status_code_200(self):
        data = self.prepare_registration_data()
        response = MyRequests.universal_method("POST", "/user/", data=data)
        Assertions.assert_code_status(response, 200)

    def test_create_user_json_has_key(self):
        data = self.prepare_registration_data()
        response = MyRequests.universal_method("POST", "/user/", data=data)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.universal_method("POST", "/user/", data=data)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",\
            f"Unexpected response content {response.content}"


