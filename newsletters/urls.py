from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_newsletter, name='create_newsletter'),
    path('list/', views.newsletter_list, name='newsletter_list'),
    path('update/<int:pk>/', views.update_newsletter, name='update_newsletter'),
    path('delete/<int:pk>/', views.delete_newsletter, name='delete_newsletter'),
]
