from django.urls import path
from .views import register, login_user, logout_user, index

app_name = 'accounts'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]   