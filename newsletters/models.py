from django.db import models


class Client(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    comment = models.TextField()


class Newsletter(models.Model):
    SEND_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    ]
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
