from django import forms
from django.core.validators import MaxValueValidator
from .validators import validate_rok


class NowyForm(forms.Form):
    imie = forms.CharField(label="Imię", max_length=20)
    rok_urodzenia = forms.IntegerField(label="Rok urodzenia", validators=[
        MaxValueValidator(2021, message="Rok urodzenia jest większy niż 2021.")])

    # rok_urodzenia = forms.IntegerField(label="Rok urodzenia", validators=[validate_rok])


    # def clean_rok_urodzenia(self):
    #     rok = self.cleaned_data.get("rok_urodzenia")
    #     if rok > 2021:
    #         raise forms.ValidationError("Rok urodzenia jest większy niż 2021.")
    #
    #     return rok
    #
    # def clean(self):
    #     cleaned_data = super(NowyForm, self).clean()
    #     rok = self.cleaned_data.get("rok_urodzenia")
    #     if rok is not None:
    #         validate_rok(rok)
