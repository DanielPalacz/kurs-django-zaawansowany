from django.shortcuts import render
from django.http import HttpResponse

from .models import Autor, Ksiazka
from .signals import nasz_sygnal
from django.db import transaction


def index(request):
    nasz_sygnal.send(sender=None, imie="Josh")
    autor = {"imie": "Walter", "nazwisko": "White"}
    ksiazka = {"tytul": "Niebieskie cuda", "rok_wydanie": 2017}

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
