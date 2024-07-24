from django.contrib import admin

from client.models import Ordine, StradaOrdine, OggettiPizzaOrdine, OggettiBibitaOrdine
from client.forms import *

admin.site.register(Ordine)
admin.site.register(StradaOrdine)
admin.site.register(OggettiPizzaOrdine)
admin.site.register(OggettiBibitaOrdine)
