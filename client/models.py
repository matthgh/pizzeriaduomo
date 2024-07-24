from uuid import uuid4
from django.db import models
from administration.models import Bibita, Pizza
from phonenumber_field.modelfields import PhoneNumberField

from client.time_choices import scelta_ora_mezzogiorno, scelta_ora_sera


class Ordine(models.Model):
    SCELTA_CONSEGNA = [
        ("consumazione_sul_posto", "Consumazione sul posto"),
        ("ritiro", "Ritiro"),
        ("consegna_al_domicilio", "Consegna a domicilio"),
    ]

    nome = models.CharField(max_length=150)
    telefono = PhoneNumberField()
    consegna = models.CharField(choices=SCELTA_CONSEGNA, max_length=100, null=True)
    data = models.DateField(auto_now_add=True)
    token = models.UUIDField(default=uuid4())

    def __str__(self) -> str:
        return f"{self.nome} {self.data} {self.consegna}"


class OggettiPizzaOrdine(models.Model):
    ordine = models.ForeignKey(to=Ordine, on_delete=models.CASCADE)
    pizza = models.ForeignKey(to=Pizza, on_delete=models.SET_NULL, null=True)
    quantita = models.PositiveIntegerField(default=1)


class OggettiBibitaOrdine(models.Model):
    ordine = models.ForeignKey(to=Ordine, on_delete=models.CASCADE)
    bibita = models.ForeignKey(to=Bibita, on_delete=models.SET_NULL, null=True)
    quantita = models.PositiveIntegerField(default=1)


class StradaOrdine(models.Model):
    ordine = models.ForeignKey(to=Ordine, on_delete=models.CASCADE)
    strada = models.CharField(max_length=500, default="")

    def __str__(self) -> str:
        return self.strada


class RitiroOrdineMezzogiorno(models.Model):
    ordine = models.ForeignKey(to=Ordine, on_delete=models.CASCADE)
    ora = models.CharField(choices=scelta_ora_mezzogiorno(), max_length=100)

    def __str__(self) -> str:
        return self.ora


class RitiroOrdineSera(models.Model):
    ordine = models.ForeignKey(to=Ordine, on_delete=models.CASCADE)
    ora = models.CharField(choices=scelta_ora_sera(), max_length=100)

    def __str__(self) -> str:
        return self.ora
