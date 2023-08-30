from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from datetime import datetime, time, timedelta
from newsletters.models import Newsletter


class Command(BaseCommand):
    help = 'Send newsletters'

    def handle(self, *args, **options):
        now = datetime.now()
        today = now.date()
        time_now = now.time()

        newsletters_to_send = Newsletter.objects.filter(
            send_time__lt=time_now,
            status='created'
        )

        for newsletter in newsletters_to_send:
            if newsletter.send_frequency == 'daily':
                send_time = datetime.combine(today, newsletter.send_time)
                self.send_newsletter(newsletter, send_time)
            elif newsletter.send_frequency == 'weekly':
                send_time = datetime.combine(today, newsletter.send_time)
                if send_time.weekday() == today.weekday():
                    self.send_newsletter(newsletter, send_time)
            elif newsletter.send_frequency == 'monthly':
                if now.day == newsletter.send_time.day:
                    send_time = datetime.combine(today, newsletter.send_time)
                    self.send_newsletter(newsletter, send_time)

    def send_newsletter(self, newsletter, send_time):
        recipients = [client.email for client in newsletter.client_set.all()]
        send_mail(
            subject="Тема вашей рассылки",
            message="Тело вашей рассылки",
            from_email="your_email@gmail.com",
            recipient_list=recipients,
            fail_silently=False,
        )

        newsletter.status = 'sent'
        newsletter.save()
