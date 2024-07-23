from django import forms

from administration.models import Ingrediente


class IngredientiForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = "__all__"

    def clean_nome(self):
        data = self.cleaned_data.get("nome")
        ingredienti = Ingrediente.objects.all().values("nome")

        for ingrediente in ingredienti:
            if data == ingrediente["nome"]:
                raise forms.ValidationError("Ingrediente già presente nella lista!")

        return data
