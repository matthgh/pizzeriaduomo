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


def consegna_domicilio(wizard):
    cleaned_data = wizard.det_cleaned_data_for_step("0")


def ritiro_mezzogiorno(wizard):
    time = datetime.now().time()
    controllo_apertura = time.hour > 12 and time.minute > 0
    controllo_chiusura = time.hour < 13 and time.minute < 45

    return controllo_apertura and controllo_chiusura


def ritiro_sera(wizard):
    time = datetime.now().time()
    controllo_apertura = time.hour > 17 and time.minute > 45
    controllo_chiusura = time.hour < 23 and time.minute < 45

    return controllo_apertura and controllo_chiusura
