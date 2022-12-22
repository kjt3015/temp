# single_pages/urls

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.about_me),
    path('', views.lending),
]