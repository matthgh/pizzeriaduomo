from django.http import HttpResponse
from django.shortcuts import render

from formtools.wizard.views import SessionWizardView
from client.forms import OggettiBibitaOrdineForm, OggettiPizzaOrdineForm
from client.models import Ordine
from client.wizard_setup import (
    WIZARD_TEMPLATES,
    FORM_LIST,
    ritiro_mezzogiorno,
    ritiro_sera,
    consegna_domicilio,
)


class OrdineWizardView(SessionWizardView):
    form_list = FORM_LIST
    condition_dict = {4: consegna_domicilio, 5: ritiro_mezzogiorno, 6: ritiro_sera}

    def get_template_names(self):
        return [WIZARD_TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):

        # ordine = Ordine.objects.create()
        print(dict(form_list[1].data))
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
