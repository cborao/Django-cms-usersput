from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('loggedIn', views.loggedIn),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('<str:key>', views.get_content),
]

