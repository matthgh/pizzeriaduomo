from client.forms import (
    OggettiBibitaOrdineForm,
    OrdineForm,
    OggettiPizzaOrdineForm,
    RitiroOrdineMezzogiornoForm,
    RitiroOrdineSeraForm,
    StradaOrdineForm,
)

from datetime import datetime

from administration.models import Bibita, Pizza

from client.models import OggettiBibitaOrdine, OggettiPizzaOrdine

WIZARD_TEMPLATES = {
    "step1": "wizard_templates/step1.html",
    "step2": "wizard_templates/step2.html",
    "step3": "wizard_templates/step3.html",
    "step4": "wizard_templates/step4.html",
    "step5": "wizard_templates/step5.html",
    "step6": "wizard_templates/step6.html",
}

FORM_LIST = [
    ("step1", OrdineForm),
    ("step2", OggettiPizzaOrdineForm),
    ("step3", OggettiBibitaOrdineForm),
    ("step4", StradaOrdineForm),
    ("step5", RitiroOrdineMezzogiornoForm),
    ("step6", RitiroOrdineSeraForm),
]


def consegna_domicilio(wizard) -> bool:
    cleaned_data = wizard.get_cleaned_data_for_step("step1") or {}
    return cleaned_data.get("consegna", False) == "consegna_al_domicilio"


def ritiro_mezzogiorno(wizard) -> bool:
    now_time = datetime.now().time()
    orario_apertura = "12:00"
    orario_chiusura = "14:45"
    orario_apertura_obj = datetime.strptime(orario_apertura, "%H:%M").time()
    orario_chiusura_obj = datetime.strptime(orario_chiusura, "%H:%M").time()
    return orario_apertura_obj < now_time and orario_chiusura_obj > now_time


def ritiro_sera(wizard) -> bool:
    now_time = datetime.now().time()
    # now_time = datetime.strptime("18:00", "%H:%M").time()
    orario_apertura = "17:45"
    orario_chiusura = "23:45"
    orario_apertura_obj = datetime.strptime(orario_apertura, "%H:%M").time()
    orario_chiusura_obj = datetime.strptime(orario_chiusura, "%H:%M").time()
    return orario_apertura_obj < now_time and orario_chiusura_obj > now_time


CONDITION_DICT = {
    "step4": consegna_domicilio,
    "step5": ritiro_mezzogiorno,
    "step6": ritiro_sera,
}


def creazione_ordine_pizze(form_list, ordine):
    pizza_form = dict(form_list[1].data)

    id_pizza = pizza_form.get("step2-pizza")[0]
    quantita = pizza_form.get("step2-quantita")[0]

    pizza_aggiuntive = pizza_form.get("pizza")
    quantita_aggiuntiva = pizza_form.get("quantita")

    pizza = Pizza.objects.get(id=id_pizza)
    OggettiPizzaOrdine.objects.create(ordine=ordine, pizza=pizza, quantita=quantita)

    if pizza_aggiuntive and quantita_aggiuntiva:
        indice_massimo = len(pizza_aggiuntive)
        indice_corrente = 0
        for _ in range(indice_massimo):
            pizza = Pizza.objects.get(id=pizza_aggiuntive[indice_corrente])
            OggettiPizzaOrdine.objects.create(
                ordine=ordine,
                pizza=pizza,
                quantita=quantita_aggiuntiva[indice_corrente],
            )
            indice_corrente += 1


def creazione_ordine_bibite(form_list, ordine):
    bibita_form = dict(form_list[2].data)

    id_bibita = bibita_form.get("step3-bibita")[0]
    quantita = bibita_form.get("step3-quantita")[0]

    bibita_aggiuntive = bibita_form.get("bibita")
    quantita_aggiuntiva = bibita_form.get("quantita")

    bibita = Bibita.objects.get(id=id_bibita)
    OggettiBibitaOrdine.objects.create(ordine=ordine, bibita=bibita, quantita=quantita)

    if bibita_aggiuntive and quantita_aggiuntiva:
        indice_massimo = len(bibita_aggiuntive)
        indice_corrente = 0
        for _ in range(indice_massimo):
            pizza = Bibita.objects.get(id=bibita_aggiuntive[indice_corrente])
            OggettiBibitaOrdine.objects.create(
                ordine=ordine,
                bibita=bibita,
                quantita=quantita_aggiuntiva[indice_corrente],
            )
            indice_corrente += 1
