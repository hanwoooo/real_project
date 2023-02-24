from django.urls import path

from . import views

urlpatterns = [
  path('', views.ListSubway.as_view()),
  path('<int:pk>/', views.DetailSubway.as_view()),
]