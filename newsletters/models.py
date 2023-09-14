from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Client(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    comment = models.TextField()


def get_default_user():
    return None


class Newsletter(models.Model):
    SEND_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('sent', 'Отправлена'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=get_default_user()
    )
    send_time = models.TimeField()
    send_frequency = models.CharField(max_length=10, choices=SEND_CHOICES)
    status = models.CharField(max_length=20, default='created')


class Message(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body = models.TextField()


class DeliveryAttempt(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    response = models.TextField(blank=True, null=True)


class DeliveryLog(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    response = models.TextField(blank=True, null=True)


class CustomUser(AbstractUser):
    email_confirmed = models.BooleanField(default=False)



