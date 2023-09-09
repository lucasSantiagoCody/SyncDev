from django.test import TestCase
from accounts.models import CustomUser
from django.urls import reverse
from django.contrib.auth import authenticate

class ViewsTest(TestCase):

    def test_profile_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/accounts/login/?next=/accounts/profile/')

    def test_add_info_profile_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('add_info_profile'))
        self.assertRedirects(response, '/accounts/login/?next=/accounts/add_info_profile/')

    def test_save_profile_picture_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('save_profile_picture'))
        self.assertRedirects(response, '/accounts/login/?next=/accounts/save_profile_picture/')
    
    def test_edit_profile_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('edit_profile'))
        self.assertRedirects(response, '/accounts/login/?next=/accounts/edit_profile/')
    
    def test_password_change_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('password_change'))
        self.assertRedirects(response, '/accounts/login/?next=/accounts/password_change/')