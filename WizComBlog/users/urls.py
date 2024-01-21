from django.urls import path
from django.contrib.auth import views as authview

from .import views

urlpatterns = [
    path('signup/',views.signup,name='signup-users'),
    path('',authview.LoginView.as_view(template_name='users/login.html'),name='user-login'),
    path('logout/',views.logoutuser,name='user-logout'),
    path('profile/',views.profile,name='user-profile'),

]

