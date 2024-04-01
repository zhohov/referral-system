import unittest

from typing import NoReturn

from django.test import TestCase
from django.contrib.auth import get_user_model


class BaseTestCase(TestCase): 
    def setUp(self) -> NoReturn:
        super().setUp()
        self.User = get_user_model()


class UserManagerTestCase(BaseTestCase): 
    def test_create_user(self) -> NoReturn:
        user = self.User.objects.create_user(
            email='user@example.com',
            password='user_password'
        )
        
        self.assertEqual(user.email, 'user@example.com')

    def test_create_super_user(self) -> str:
        superuser = self.User.objects.create_superuser(
            email='superuser@example.com',
            password='user_password',
        )
        
        self.assertEqual(superuser.email,'superuser@example.com')
        self.assertEqual(superuser.is_superuser, True)
        self.assertEqual(superuser.is_staff, True)

    def test_create_user_extra_fields(self) -> NoReturn:
        user = self.User.objects.create_user(
            username='user',
            email='user1@example.com',
            password='user_password',
        )

        self.assertEqual(user.username, 'user')

    def test_create_superuser_extra_fields(self) -> NoReturn:
        superuser = self.User.objects.create_superuser(
            username='superuser',
            email='superuser1@example.com',
            password='user_password',
        )

        self.assertEqual(superuser.username,'superuser')


class UserManagerFailureTestCase(BaseTestCase): 
    @unittest.expectedFailure
    def test_create_user_without_email(self) -> NoReturn:
        with self.assertRaises(ValueError):
            self.User.objects.create_user(
                username='user',
                password='user_password'
            )
    
    @unittest.expectedFailure
    def test_create_superuser_without_email(self) -> NoReturn:
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                username='superuser',
                password='user_password'
            )              

    @unittest.expectedFailure
    def test_create_user_without_password(self) -> NoReturn:
        with self.assertRaises(ValueError):
            self.User.objects.create_user(
                username='user',
                email='user1@example.com'
            )

    @unittest.expectedFailure
    def test_create_superuser_without_password(self) -> NoReturn:
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                username='superuser',
                email='superuser1@example.com'
            )
