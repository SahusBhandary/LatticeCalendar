from django.test import TestCase
from django.contrib.auth import get_user_model

# User Management Tests
class UserManagementTests(TestCase):

    def test_create_user(self):
        # Create Default User
        User = get_user_model()
        user = User.objects.create_user(username="test", email="test@gmail.com", password="123")

        # Check the fields match what a default user should have
        self.assertEqual(user.email, "test@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
        # Check required fields
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="", password="")
        with self.assertRaises(TypeError):
            User.objects.create_user(username="", password="")
        with self.assertRaises(TypeError):
            User.objects.create_user(username="", email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(username="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(password="")

    def test_create_super_user(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="super@user.com", password="foo", is_superuser=False)
    
    
        
        
        
        





