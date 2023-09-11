from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from newsletters.models import Newsletter
from django.views.decorators.cache import cache_page


def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blog/blog_post_list.html', context)


def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_post_detail.html', {'post': post})


@cache_page(60 * 15)  # Кешировать на 15 минут (время в секундах)
def home(request):
    # Получите данные для отображения на главной странице
    total_newsletters = Newsletter.objects.count()
    active_newsletters = Newsletter.objects.filter(status='active').count()
    unique_clients = Newsletter.objects.values('user').distinct().count()
    random_blog_posts = BlogPost.objects.order_by('?')[:3]  # Получите 3 случайные статьи блога

    context = {
        'total_newsletters': total_newsletters,
        'active_newsletters': active_newsletters,
        'unique_clients': unique_clients,
        'random_blog_posts': random_blog_posts,
    }

    return render(request, 'home.html', context)
