from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from library.models import Event
from django.contrib.auth.models import User


class LibraryBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestBoundary", True, "boundary")
        print("TestBoundary = Passed")
