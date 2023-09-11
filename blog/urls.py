from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_post_list, name='blog_post_list'),  # URL для списка статей блога
    path('<int:pk>/', views.blog_post_detail, name='blog_post_detail'),  # URL для детальной страницы статьи
    path('home/', views.home, name='home'),  # URL для главной страницы
]
