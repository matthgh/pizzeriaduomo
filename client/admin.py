from django.contrib import admin

from client.models import *
from client.forms import *

classes = [
    Ordine,
    StradaOrdine,
    OggettiPizzaOrdine,
    OggettiBibitaOrdine,
    RitiroOrdineMezzogiorno,
    RitiroOrdineSera,
]

for _class in classes:
    admin.site.register(_class)
