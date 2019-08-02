from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('new/', views.register_user, name='new'),
    path('register/', views.confirm_register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('auth/', views.confirm_login_user, name='auth'),
]