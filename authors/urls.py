from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/token', obtain_auth_token, name='obtain-auth-token'),
    path('register/', views.RegisterView.as_view(), name='register-author'),

]
