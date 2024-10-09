from django.shortcuts import render
from django.http import HttpResponse

from .models import Autor, Ksiazka
from .signals import nasz_sygnal
from django.db import transaction
from django.core.mail import send_mail
# from .email_check import wyslij_email

from django.contrib import messages


def index(request):
    nasz_sygnal.send(sender=None, imie="Josh")
    autor = {"imie": "Walter", "nazwisko": "White"}
    ksiazka = {"tytul": "Niebieskie cuda", "rok_wydania": 2017}

    dodaj_do_bazy(autor, ksiazka)
    return HttpResponse("Główna strona.")


# def dodaj_do_bazy(autor, ksiazka):
#     nowy_autor = Autor.objects.create(**autor)
#     nowa_ksiazka = Ksiazka(**ksiazka)
#     nowa_ksiazka.autor = nowy_autor
#     nowa_ksiazka.save()

# @transaction.atomic()
# def dodaj_do_bazy(autor, ksiazka):
#     nowy_autor = Autor.objects.create(**autor)
#     nowa_ksiazka = Ksiazka(**ksiazka)
#     nowa_ksiazka.autor = nowy_autor
#     nowa_ksiazka.save()


# @transaction.non_atomic_requests
def dodaj_do_bazy(autor, ksiazka):
    with transaction.atomic():
        nowy_autor = Autor.objects.create(**autor)
        nowa_ksiazka = Ksiazka(**ksiazka)
        nowa_ksiazka.autor = nowy_autor
        nowa_ksiazka.save()

#
# def email(request):
#     wyslij_email()
#     return HttpResponse("Wysyłka testowego emaila.")


# def email(request):
#     if request.method == "POST":
#         if request.POST.get("email", False):
#             email = request.POST["email"]
#
#             subject = 'Testowy email z Django'
#             message = 'To jest testowa wiadomość wysłana z Django.'
#             email_from = "daniel.palacz@pyx.solutions"
#             recipient_list = ['daniel.palacz@gmail.com', email]
#
#             send_mail(subject, message, email_from, recipient_list, fail_silently=False)
#             return HttpResponse(f"Wysłano testowego emaila. Adresaci: {recipient_list}")
#
#     return render(request, "biblioteka/email_form.html")

def email(request):
    if request.method == "POST":
        if request.POST.get("email", False):
            email = request.POST["email"]

            subject = 'Testowy email z Django - lista książek.'
            ksiazki = ", ".join([ksiazka.tytul for ksiazka in Ksiazka.objects.all()])
            message = '<h1>To jest nowa testowa wiadomość wysłana z Django.</h1> Lista książek: ' + ksiazki
            email_from = "daniel.palacz@pyx.solutions"
            recipient_list = ['daniel.palacz@gmail.com', email]

            try:
                send_mail(subject, message, email_from, recipient_list, fail_silently=False, html_message=message)
                # return HttpResponse(f"Wysłano testowego emaila. Adresaci: {recipient_list}")

                messages.success(request, f"Wysłano testowego emaila. Adresaci: {recipient_list}")
            except Exception as e:
                messages.error(request, f"Nie wysłano testowego emaila. Adresaci: {recipient_list}. Błąd: {type(e)}")


    return render(request, "biblioteka/email_form.html")
