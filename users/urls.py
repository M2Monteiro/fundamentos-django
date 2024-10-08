from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register", views.register_view, name="register"),  # users:register
    path("login", views.login_view, name="login"),  # users:login
    path('logout', views.logout_view, name="logout"), #users:logout
]
