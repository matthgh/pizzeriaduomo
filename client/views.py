from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from formtools.wizard.views import SessionWizardView

from client.forms import OggettiBibitaOrdineForm, OggettiPizzaOrdineForm
from client.models import Ordine, OggettiPizzaOrdine, OggettiBibitaOrdine
from client.wizard_setup import WIZARD_TEMPLATES, FORM_LIST, CONDITION_DICT

from administration.models import Pizza


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

        else:
            ordine = form_ordine.save()

        pizza_form = dict(form_list[1].data)

        id_pizza = pizza_form.get("step2-pizza")[0]
        quantita = pizza_form.get("step2-quantita")[0]
        pizza = get_object_or_404(Pizza, id=id_pizza)
        print(pizza)
        OggettiPizzaOrdine.objects.create(ordine=ordine, pizza=pizza, quantita=quantita)

        print(dict(form_list[1].data))

        print(form_list)
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
