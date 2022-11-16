
from django.contrib import admin
from django.urls import path
from core.views import HomeView,SingUpView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('singup/',SingUpView.as_view(),name='singup'),
    path('admin/', admin.site.urls),
]
