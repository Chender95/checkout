from . views import bomba
from blog import views
from django.urls import path, include

urlpatterns = [
    path('', views.bomba, name='index')
]