from django.core.mail import send_mail
from django.utils import timezone
from django_cron import CronJobBase, Schedule
from newsletters.models import Newsletter


class SendNewslettersCron(CronJobBase):
    RUN_AT_TIMES = ['00:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'newsletters.send_newsletters_cron'

    def do(self):
        now = timezone.now()
        newsletters_to_send = Newsletter.objects.filter(
            send_time__lt=now.time(),
            status='created'
        )

        for newsletter in newsletters_to_send:
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
