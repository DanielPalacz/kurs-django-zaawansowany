from array import array

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver, Signal
from django.core.signals import request_finished
from .models import Autor
import logging



autor_log = logging.getLogger("autor_log")
autor_log.setLevel(logging.DEBUG)
autor_handler = logging.FileHandler("logs/autor.log")
autor_handler.setLevel(logging.DEBUG)
autor_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s %(message)s")
autor_handler.setFormatter(autor_formatter)
autor_log.addHandler(autor_handler)


nasz_sygnal = Signal()


@receiver([post_save], sender=Autor)
def autor_po_zapisaniu(sender, instance, **kwargs):
    print("Właśnie zapisaliśmy autora.")
    print(instance.imie)
    autor_log.info(f"Właśnie zapisaliśmy autora '{instance.imie} {instance.nazwisko}'.")


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
