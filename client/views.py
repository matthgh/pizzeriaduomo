from django.http import HttpResponse
from django.shortcuts import render

from formtools.wizard.views import SessionWizardView
from client.forms import OggettiBibitaOrdineForm, OggettiPizzaOrdineForm
from client.models import Ordine
from client.wizard_setup import WIZARD_TEMPLATES, FORM_LIST, CONDITION_DICT


class OrdineWizardView(SessionWizardView):
    form_list = FORM_LIST
    condition_dict = CONDITION_DICT

    def get_template_names(self):
        return [WIZARD_TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_ordine = form_list[0]
        if form_ordine.cleaned_data.get("consegna") == "consegna_al_domicilio":
            ordine = form_ordine.save()
            consegna = form_list[4].save(commit=False)
            consegna.ordine = ordine
            x = consegna.save()
            print(x)

        else:
            form_ordine.save()

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
