###### Django 3: zaawansowany kurs po polsku (PL)
###### https://github.com/Nogostradamus/kurs-django-zaawansowany




## Wprowadzenie - Django shell

```
Django shell

Zainstalowanie i skonfigurowanie django-extensions / ipython (requirements_extended.txt):
 - python manage.py shell_plus
 - python manage.py shell_plus --ipython
```

## ORM: Metody ORM

```
 - domyślny manager 'objects'
 - Ksiazka.objects.all()
 - Ksiazka.objects.filter(rok_wydania=1950)
 - Ksiazka.objects.exclude(rok_wydania=1950)
 - Ksiazka.objects.order_by("rok_wydania")
 - Ksiazka.objects.order_by("-rok_wydania")
 - Ksiazka.objects.exclude(rok_wydania=1950).order_by("tytul")
```


## ORM: limitowanie rekordów

```
 - Ksiazka.objects.first()
 - Ksiazka.objects.last()
 - Ksiazka.objects.all()[:3]
 - Ksiazka.objects.all()[3:]
```


## ORM: filtrowianie na podstawie fields
```
 - Ksiazka.objects.filter(rok_wydania=1960)
 - Ksiazka.objects.filter(rok_wydania__exact=1960)
 - Ksiazka.objects.filter(tytul__exact="Zagubiona podkowa")
 - Ksiazka.objects.filter(tytul__iexact="zagubiona podkowa")
 - Ksiazka.objects.filter(rok_wydania__gt=1959)
 - Ksiazka.objects.filter(rok_wydania__lt=1959)
 - Ksiazka.objects.filter(rok_wydania__lte=1960)
 - Autor.objects.filter(data_urodzenia__year=1990)
 - Autor.objects.filter(data_urodzenia__isnull=True)
 - Autor.objects.filter(imie__contains="a")
 - Autor.objects.filter(imie__icontains="a")
 - Autor.objects.filter(imie__startswith="M")
 - Autor.objects.filter(imie__endswith="l")
 - Autor.objects.filter(imie__contains="a", nazwisko__startswith="E")
```



## ORM: więcej metod na pozyskiwanie danych
```
 - Ksiazka.objects.filter(rok_wydania=2001).exists()
 - Ksiazka.objects.order_by("-tytul")
 - Ksiazka.objects.order_by("tytul").reverse()
 - Ksiazka.objects.all()
 - Ksiazka.objects.all().values()
 - Ksiazka.objects.all().values_list()
 - Ksiazka.objects.all().defer("autor", "id")
 - Ksiazka.objects.all().only("autor")
 - Autor.objects.dates("data_urodzenia", "year")
 - Autor.objects.dates("data_urodzenia", "month")
 - <Model>.objects.datetime("created", "hour")
```



## ORM: używanie relationship
```
 - Autor.objects.filter(id__in=[2,3])
 - Ksiazka.objects.get(pk=1).autor.imie
 - Ksiazka.objects.filter(autor=1)
 - Autor.objects.get(id=1).ksiazki.all()
 - Autor.objects.get(id=1).ksiazki.count()
 - Ksiazka.objects.filter(autor__imie__contains="a")
 - Ksiazka.objects.filter(autor__data_urodzenia__year__gte=1960)
```



## ORM: działania matematyczne
```
 - autorzy = Autor.objects.annotate(ilosc_ksiazek=Count("ksiazki"))
 - autorzy[0].ilosc_ksiazek
 - Ksiazka.objects.aggregate(Avg("rok_wydania"), Max("rok_wydania"), Min("rok_wydania"), Count("rok_wydania"))
```

## ORM: zmienianie rekordów
```
 - nowa_ksiazka = Ksiazka.objects.create(tytul="Idiota", rok_wydania=1980, autor=dostojewski)
 - ksiazka2 = Ksiazka(tytul="Wszystko o kotach", rok_wydania=2020)
 - autor2 = Autor(imie="Moutou", nazwisko="Francois")
 - autor2.save()
 - ksiazka2.autor = autor2
 - ksiazka.save()
```

## ORM: sprawne zmienianie
```
 - autor, created = Autor.objects.get_or_create(imie="Norman", nazwisko="Bates")
 - autor, created = Autor.objects.update_or_create(imie="Norman", nazwisko="Bates", defaults={"data_urodzenia":"1944-02-08"})
 - Autor.objects.bulk_create([Autor(imie="Walter", nazwisko="White"), Autor(imie="Albus", nazwisko="Dumbledore")])
 - Autor.objects.bulk_update(...)
```

## ORM: choices
```
 - ksiazka.get_gatunek_display()
```

## Modele: Managers
```
 - tworzenie customowych model managerów
```

## Modele: Queryset dla managers
```
 - tworzenie class-based queryset
```

## Modele: Meta class dla modeli
```
 - <model>.Meta.db_table
 - <model>.Meta.ordering
 - <model>.Meta.verbose_name
 - <model>.Meta.verbose_name_plural
 - <model>.Meta.unique_together
 - <model>.Meta.indexes
 - <model>.Meta.permissions
```


## Modele: Signals
```
 - from django.db.models.signals import post_save, pre_save
 - from django.dispatch import receiver
```

## Modele: Signal instance


## Modele: Wczytywanie signals

## Modele: Request i własny signal
```
 - request_finished
 - customowy sygnał
```

## Modele: Transakcje
```
 - w Django jest domyślnie ustawione 'auto commit true'
 - @transaction.atomic()
```