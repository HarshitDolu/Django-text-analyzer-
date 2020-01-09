#urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('register',views.register,name='register'),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
]