from django import forms

from client.models import *


class OrdineForm(forms.ModelForm):
    class Meta:
        model = Ordine
        exclude = ("token", "date")


class OggettiPizzaOrdineForm(forms.ModelForm):
    class Meta:
        model = OggettiPizzaOrdine
        exclude = ("ordine",)


class OggettiBibitaOrdineForm(forms.ModelForm):
    class Meta:
        model = OggettiBibitaOrdine
        exclude = ("ordine",)


class StradaOrdineForm(forms.ModelForm):
    class Meta:
        model = StradaOrdine
        exclude = ("ordine",)


class RitiroOrdineMezzogiornoForm(forms.ModelForm):
    class Meta:
        model = RitiroOrdineMezzogiorno
        exclude = ("ordine",)


class RitiroOrdineSeraForm(forms.ModelForm):
    class Meta:
        model = RitiroOrdineSera
        exclude = ("ordine",)
