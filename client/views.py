from django.http import HttpResponse
from django.shortcuts import render

from formtools.wizard.views import SessionWizardView

from client.forms import OggettiBibitaOrdineForm, OggettiPizzaOrdineForm
from client.models import Ordine, OggettiPizzaOrdine, OggettiBibitaOrdine
from client.wizard_setup import (
    WIZARD_TEMPLATES,
    FORM_LIST,
    CONDITION_DICT,
    creazione_ordine_bibite,
    creazione_ordine_pizze,
)


class OrdineWizardView(SessionWizardView):
    form_list = FORM_LIST
    condition_dict = CONDITION_DICT

    def get_template_names(self):
        return [WIZARD_TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_ordine = form_list[0]
        if form_ordine.cleaned_data.get("consegna") == "consegna_al_domicilio":
            ordine = form_ordine.save()
            strada_consegna = form_list[3].save(commit=False)
            strada_consegna.ordine = ordine
            strada_consegna.save()
            orario = form_list[4].save(commit=False)
            orario.ordine = ordine
            orario.save()

        else:
            ordine = form_ordine.save()
            orario = form_list[3].save(commit=False)
            orario.ordine = ordine
            orario.save()

        creazione_ordine_pizze(form_list=form_list, ordine=ordine)
        creazione_ordine_bibite(form_list=form_list, ordine=ordine)

        print(form_list[3].data)

        return HttpResponse("Done method!")


def additional_pizza_form(request):
    return render(
        request,
        "partials/additional_pizza_form.html",
        {"form": OggettiPizzaOrdineForm()},
    )


def additional_bibita_form(request):
    return render(
        request,
        "partials/additional_bibita_form.html",
        {"form": OggettiBibitaOrdineForm()},
    )
