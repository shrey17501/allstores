from django.urls import path
from . import views

urlpatterns = [
    path("electronic", views.electronic, name='electronic'),
    path("supermarket", views.supermarket, name='supermarket'),
    path("movietheater", views.movietheater, name='movietheater'),
    path("automobile", views.automobile, name='automobile'),
    path("telecom", views.telecom, name='telecom'),
    path("home/", views.home, name="home"),
    path("", views.loginUser, name="login"),
    path("signup", views.signup, name="signup"),
    path('logout',views.logoutUser, name="logout")
]
