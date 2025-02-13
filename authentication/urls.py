# authentication/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', view=views.signup_view, name='signup_view'),
    path('login/', view=views.login_view, name='login_view'),
    path('signout/', view=views.logout_view, name='logout_view'),   
]
