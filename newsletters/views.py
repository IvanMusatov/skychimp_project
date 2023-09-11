from django.shortcuts import render, redirect
from .models import Newsletter
from .forms import NewsletterForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


def create_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter_list')
    else:
        form = NewsletterForm()
    return render(request, 'newsletters/newsletter_form.html', {'form': form})


def newsletter_list(request):
    newsletters = Newsletter.objects.all()
    return render(request, 'newsletters/newsletter_list.html', {'newsletters': newsletters})


def update_newsletter(request, pk):
    newsletter = Newsletter.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewsletterForm(request.POST, instance=newsletter)
        if form.is_valid():
            form.save()
            return redirect('newsletter_list')
    else:
        form = NewsletterForm(instance=newsletter)
    return render(request, 'newsletters/newsletter_form.html', {'form': form})


def delete_newsletter(request, pk):
    newsletter = Newsletter.objects.get(pk=pk)
    if request.method == 'POST':
        newsletter.delete()
        return redirect('newsletter_list')
    return render(request, 'newsletters/newsletter_confirm_delete.html', {'newsletter': newsletter})


def is_manager(user):
    return user.is_authenticated and user.is_manager


# Просмотр всех рассылок
@user_passes_test(is_manager)
def view_all_newsletters(request):
    newsletters = Newsletter.objects.all()
    return render(request, 'manager/view_all_newsletters.html', {'newsletters': newsletters})


# Просмотр списка пользователей
@user_passes_test(is_manager)
def view_user_list(request):
    users = User.objects.all()
    return render(request, 'manager/view_user_list.html', {'users': users})


# Блокировка пользователей
@user_passes_test(is_manager)
def block_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    return redirect('view_user_list')


# Отключение рассылок
@user_passes_test(is_manager)
def disable_newsletter(request, newsletter_id):
    newsletter = Newsletter.objects.get(pk=newsletter_id)
    newsletter.status = 'disabled'
    newsletter.save()
    return redirect('view_all_newsletters')
