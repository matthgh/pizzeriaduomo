from django.contrib import admin

from administration.models import Ingrediente, Pizza, Bibita
from administration.forms import IngredientiForm

admin.site.register(Pizza)
admin.site.register(Bibita)


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    form = IngredientiForm
