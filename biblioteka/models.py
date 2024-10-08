from django.db import models

# from biblioteka.managers import KsiazkaNowoczesnaManager
# from biblioteka.managers import KsiazkaStaraManager
from biblioteka.managers import KsiazkaManager


class Autor(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    nazwisko = models.CharField(max_length=20, blank=False)
    data_urodzenia = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.imie + " " + self.nazwisko


class Gatunek:
    NIEZNANY = 0
    FANTASY = 1
    HORROR = 2
    DRAMA = 3

    GATUNKI = (
        (NIEZNANY, "Nieznany"),
        (FANTASY, "Fantasy"),
        (HORROR, "Horror"),
        (DRAMA, "Drama"),
    )



class Ksiazka(models.Model):

    tytul = models.CharField(max_length=50, blank=False)
    rok_wydania = models.IntegerField(blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="ksiazki")
    gatunek = models.PositiveSmallIntegerField(choices=Gatunek.GATUNKI, default=0)

    objects = models.Manager()
    # nowoczesne = KsiazkaNowoczesnaManager()
    # stare = KsiazkaStaraManager()
    ksiazki = KsiazkaManager()

    def __str__(self):
        return self.tytul

    class Meta:
        # db_table = "ksiazki"
        ordering = ("-rok_wydania",)
        verbose_name = "Książka"
        verbose_name_plural = "Książki"
        unique_together = ["tytul", "rok_wydania"]
        indexes = [
            models.Index(fields=["tytul"], name="tytul_index"),
            models.Index(fields=["rok_wydania"]),
        ]
        permissions = [
            ("can_update_ksiazka", "Może zmieniać książke")
        ]
