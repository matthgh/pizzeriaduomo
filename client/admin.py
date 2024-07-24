from django.contrib import admin

from client.models import Ordine, StradaOrdine
from client.forms import *

admin.site.register(Ordine)
admin.site.register(StradaOrdine)
