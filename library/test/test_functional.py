from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from library.models import Event
from rest_framework.test import APITestCase
from django.test import TestCase
from django.http import HttpResponse
from django.contrib.auth.models import User

class UserFunctionalTest(APITestCase):

    def test_user_registration_and_logging(self):
        """Test if user registration triggers the logging of details."""
        test_obj = TestUtils()
        try:
            # Create the user
            user_data = {
                'username': 'testuser',
                'password': 'password123',
                'email': 'testuser@example.com'
            }
            user = User.objects.create_user(**user_data)

            # Check if the correct log entry is created
            with open('user_registration.log', 'r') as log_file:
                logs = log_file.readlines()
            log_message = f"User Registered: {user.username}, Email: {user.email}"

            self.assertTrue(any(log_message in log for log in logs))
            test_obj.yakshaAssert("TestUserRegistrationAndLogging", True, "functional")
            print("TestUserRegistrationAndLogging = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestUserRegistrationAndLogging", False, "functional")
            print(f"TestUserRegistrationAndLogging = Failed")
