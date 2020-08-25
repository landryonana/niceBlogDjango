from django.urls import path
from django.contrib.auth import views as auth_views


from . import views
from .forms import LoginForm


app_name = 'accounts'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(
        authentication_form=LoginForm),
        name='account_login'),

    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),

    path('register/', views.account_register, name='account_register'),

    path('user/profile/', views.account_profile, name='account_profile'),

]
