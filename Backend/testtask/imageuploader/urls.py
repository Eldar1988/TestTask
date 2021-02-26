from django.urls import path
from . import views

urlpatterns = [
    path('images/<int:pk>/', views.ImageListView.as_view()),
    path('image_actions/<int:pk>/', views.ImageActionsView.as_view()),
]
