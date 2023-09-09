from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('add_info_profile/', views.add_info_profile, name='add_info_profile'),
    path('save_profile_picture/', views.save_profile_picture, name='save_profile_picture'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('password_change/', views.password_change, name='password_change'),

    # auth  views for reset password
    path('password_reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset/done/', views.ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.ResetPasswordCompleteView.as_view(), name='password_reset_complete'),
    
]


