from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_newsletter, name='create_newsletter'),
    path('list/', views.newsletter_list, name='newsletter_list'),
    path('update/<int:pk>/', views.update_newsletter, name='update_newsletter'),
    path('delete/<int:pk>/', views.delete_newsletter, name='delete_newsletter'),
    path('view_all_newsletters/', views.view_all_newsletters, name='view_all_newsletters'),
    path('view_user_list/', views.view_user_list, name='view_user_list'),
    path('block_user/<int:user_id>/', views.block_user, name='block_user'),
    path('disable_newsletter/<int:newsletter_id>/', views.disable_newsletter, name='disable_newsletter'),
]
