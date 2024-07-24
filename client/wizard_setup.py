from client.forms import (
    OggettiBibitaOrdineForm,
    OrdineForm,
    OggettiPizzaOrdineForm,
    RitiroOrdineMezzogiornoForm,
    RitiroOrdineSeraForm,
    StradaOrdineForm,
)

from datetime import datetime

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
    orario_chiusura = "13:45"
    orario_apertura_obj = datetime.strptime(orario_apertura, "%H:%M").time()
    orario_chiusura_obj = datetime.strptime(orario_chiusura, "%H:%M").time()
    return orario_apertura_obj < now_time and orario_chiusura_obj > now_time


def ritiro_sera(wizard) -> bool:
    # now_time = datetime.now().time()
    now_time = datetime.strptime("18:00", "%H:%M").time()
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
