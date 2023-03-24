from django.test import TestCase
from ..forms import UserRegisterForm


class TestUserForm(TestCase):
    """Test registration form"""


    def test_valid_registration_data(self):
        """Tests registration with valid data"""

        form_data = {
            "username": "test_user",
            "email": "test_user@test.com",
            "password1": "Userpass0101",
            "password2": "Userpass0101"
        }
        form = UserRegisterForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_invalid_registration_data(self):
        """Tests registration with invalid data"""

        form_data = {
            "username": "test_user",
            "email": "test_usercom", #invalid e-mail
            "password1": "Userpass0101",
            "password2": "Userpass0101"
        }
        form = UserRegisterForm(data=form_data)
        
        self.assertFalse(form.is_valid())

    def test_common_password(self):
        """Tests registration with invalid data"""

        form_data = {
            "username": "test_user",
            "email": "test_user@test.com", 
            "password1": "testpass", #invalid, common password
            "password2": "testpass"
        }
        form = UserRegisterForm(data=form_data)
        
        self.assertFalse(form.is_valid())

