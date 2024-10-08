from os import getenv

from django.core.mail import send_mail
from django.conf import settings


def wyslij_email():
    subject = 'Testowy email z Django'
    message = 'To jest testowa wiadomość wysłana z Django.'
    email_from = "daniel.palacz@pyx.solutions"
    recipient_list = ['daniel.palacz@gmail.com', "saweg34339@paxnw.com"]

    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
