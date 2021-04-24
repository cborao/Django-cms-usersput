from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView as login

urlpatterns = [
    path('cms/', include('cms.urls')),
    path('admin/', admin.site.urls),
    path('login', login.as_view()),
]
