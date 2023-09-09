from django.test import TestCase
from accounts.models import CustomUser, Profile 
from django.contrib.auth import authenticate

class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(username='test', email='test@gmail.com', password='initialtest')
        global user 
        user = CustomUser.objects.get(id=1)
    
    def test_email_max_length(self):
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 40)
    def test_email_label(self):
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')
    def test_username_max_length(self):
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 30)
    def test_username_label(self):
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')
    
    
class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(username='test', email='test@gmail.com', password='initialtest')
        global userprofile
        userprofile = Profile.objects.get(user=1)
    
    def test_phone_max_length(self):
        max_length = userprofile._meta.get_field('phone').max_length
        self.assertEquals(max_length, 13)
    def test_phone_label(self):
        field_label = userprofile._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')
    def test_nif_max_length(self):
        max_length = userprofile._meta.get_field('nif').max_length
        self.assertEquals(max_length, 14)
    def test_nif_label(self):
        field_label = userprofile._meta.get_field('nif').verbose_name
        self.assertEquals(field_label, 'nif')
    def test_user_label(self):
        field_label = userprofile._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'user')
    def test_date_of_birth_label(self):
        field_label = userprofile._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')
    def test_profilepicture_label(self):
        field_label = userprofile._meta.get_field('profile_picture').verbose_name
        self.assertEquals(field_label, 'profile picture')