from django.urls import path
from django.contrib.auth.views import logout
from . import views

app_name = "forumsApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("loginView/",views.loginView, name="loginView"),
    path("signup/", views.signup, name="signup"),
    path("logoutView/", views.logoutView, name="logout"),
    path("accounts/profile/", views.index, name="profile"),
]