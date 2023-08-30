from django.shortcuts import render, redirect
from .models import Newsletter
from .forms import NewsletterForm


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
