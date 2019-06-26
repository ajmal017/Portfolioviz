from django.urls import path
from . import views

urlpatterns = [
    path('', views.research_home, name='research_home'),
]


