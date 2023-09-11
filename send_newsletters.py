from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from newsletters.models import Newsletter, DeliveryLog


class Command(BaseCommand):
    help = 'Send newsletters'

    def handle(self, *args, **options):
        now = timezone.now()

        newsletters_to_send = Newsletter.objects.filter(
            send_time__lte=now.time(),
            end_time__gt=now.time(),
            status='launched'
        )

        for newsletter in newsletters_to_send:
            if newsletter.send_frequency == 'daily':
                self.send_newsletter(newsletter)
            elif newsletter.send_frequency == 'weekly':
                if now.weekday() == newsletter.send_time.weekday():
                    self.send_newsletter(newsletter)
            elif newsletter.send_frequency == 'monthly':
                if now.day == newsletter.send_time.day:
                    self.send_newsletter(newsletter)

    def send_newsletter(self, newsletter):
        recipients = [client.email for client in newsletter.client_set.all()]
        try:
            send_mail(
                subject=newsletter.message_set.first().subject,
                message=newsletter.message_set.first().body,
                from_email="your_email@gmail.com",
                recipient_list=recipients,
                fail_silently=False,
            )
            status = 'sent'
            response = 'Message sent successfully'
        except Exception as e:
            status = 'failed'
            response = str(e)

        log_entry = DeliveryLog.objects.create(
            newsletter=newsletter,
            status=status,
            response=response
        )

        newsletter.status = 'sent'
        newsletter.save()