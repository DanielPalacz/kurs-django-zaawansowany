from array import array

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver, Signal
from django.core.signals import request_finished
from .models import Autor


nasz_sygnal = Signal()


@receiver([post_save], sender=Autor)
def autor_po_zapisaniu(sender, instance, **kwargs):
    print("Właśnie zapisaliśmy autora.")
    print(instance.imie)


@receiver([pre_save], sender=Autor)
def autor_przed_zapisaniu(sender, instance, **kwargs):
    try:
        nasz_autor = Autor.objects.get(id=instance.id)
        print("Za chwilę zapiszemy autora.")
        print(nasz_autor.imie)
    except Autor.DoesNotExist:
        print(f"Za chwilę stworzymy nowego autora ({instance.imie}).")


@receiver(request_finished)
def strona_wczytana(sender, **kwargs):
    print("Strona została wczytana.")


@receiver(nasz_sygnal)
def podane_imie(sender, **kwargs):
    print(f"Otrzymano sygnał z '{sender}' z argumentami: {kwargs}")
    print(f"Podano imię {kwargs['imie']}.")



# @receiver([pre_save, post_save], sender=Autor)
# def autor_po_zapisaniu(sender, instance, **kwargs):
#     print("Właśnie zapisaliśmy autora.")
#     print(instance.imie)


# def autor_po_zapisaniu(sender, instance, **kwargs):
#     print("Właśnie zapisaliśmy autora.")


# post_save.connect(autor_po_zapisaniu, sender=Autor)
