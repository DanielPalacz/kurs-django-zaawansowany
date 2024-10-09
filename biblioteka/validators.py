from django.core.exceptions import ValidationError

def validate_rok(value):
    if value > 2020:
        raise ValueError("Rok jest większy niz 2018.")
    return value
