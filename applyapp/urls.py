from django.urls import path
from . import views

urlpatterns =[
    path('application/', views.ApplyListView.as_view()),
]