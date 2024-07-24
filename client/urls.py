from django.urls import path

from client import views


urlpatterns = [
    path("", view=views.OrdineWizardView.as_view()),
    path(
        "additional_pizza_form/",
        views.additional_pizza_form,
        name="additional-pizza-form",
    ),
    path(
        "additional_bibita_form/",
        views.additional_bibita_form,
        name="additional-bibita-form",
    ),
]
