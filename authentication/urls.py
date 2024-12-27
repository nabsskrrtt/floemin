from django.urls import path
from authentication.views import get_user, login, logout, register

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('get_user/', get_user,name='get_user')
]