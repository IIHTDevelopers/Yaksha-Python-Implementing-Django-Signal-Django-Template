from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from django.contrib.auth.models import User


class UserExceptionalTest(APITestCase):

    def test_user_registration_missing_email(self):
        """Test if the signal works properly when the email is missing."""
        test_obj = TestUtils()
        try:
            user_data = {
                'username': 'testuser2',
                'password': 'password123'
            }
            user = User.objects.create_user(**user_data)

            # Check if the log file contains the appropriate message, even with missing email
            with open('user_registration.log', 'r') as log_file:
                logs = log_file.readlines()
            log_message = f"User Registered: {user.username}, Email: "

            self.assertTrue(any(log_message in log for log in logs))
            test_obj.yakshaAssert("TestUserRegistrationMissingEmail", True, "exceptional")
            print("TestUserRegistrationMissingEmail = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestUserRegistrationMissingEmail", False, "exceptional")
            print(f"TestUserRegistrationMissingEmail = Failed")
