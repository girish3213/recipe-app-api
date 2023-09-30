"""
Tests for the Django admin modifications 
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    """
    Test cases for the admin site
    """
    def setUp(self):
        """Setup function for the admin site tests"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@example.com',
            password = 'testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'user@example.com',
            password = 'testpass123',
            name = 'Test User'
        )
        
    def test_users_list(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        # This reverse function will generate the url for our list user page
        # appname_modelname_changelist
        # This is the url that will be generated: /admin/core/user/
        res = self.client.get(url)
        # This will perform a http get on the url
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test that the edit user page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # This will generate the url for the edit user page
        # appname_modelname_change
        # This is the url that will be generated: /admin/core/user/1
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    
    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        # This will generate the url for the create user page
        # appname_modelname_add
        # This is the url that will be generated: /admin/core/user/add
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    