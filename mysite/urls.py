
from django.contrib import admin
from django.urls import path,include
from core.views import HomeView,singup,secret_page,SecretPage

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('singup/',singup,name='singup'),
    path('secret/',secret_page,name='secret_page'),
    path('secret2/',SecretPage.as_view(),name='secret'),
    path('acocont/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
