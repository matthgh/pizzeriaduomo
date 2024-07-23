from django.db import models


class CategoriePizza(models.IntegerChoices):
    PIZZE_BASI = 1
    PIZZE_SPECIALITA = 2
    PIZZE_SPECIALI_BIANCHE = 3
    PIZZE_NOVITA = 4


class CategorieBibita(models.IntegerChoices):
    BIBITA_PICCOLA = 1
    BIBITA_GRANDE = 2


class Ingrediente(models.Model):
    nome = models.CharField(default="", max_length=100)

    def __str__(self) -> str:
        return self.nome


# class PizzaAlMetro(models.Model):
#     pass


class Pizza(models.Model):
    nome = models.CharField(default="", max_length=100)
    ingredienti = models.ManyToManyField(Ingrediente)
    prezzo = models.FloatField()
    categoria = models.IntegerField(
        choices=CategoriePizza.choices, default=CategoriePizza.PIZZE_BASI
    )
    url_immagine = models.URLField(default="", blank=True)

    def __str__(self) -> str:
        return self.nome


class PizzeBase(Pizza):
    class Meta:
        proxy = True

    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(categoria=CategoriePizza.PIZZE_BASI)

    objects = Manager()


class PizzeSpecialita(Pizza):
    class Meta:
        proxy = True

    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return (
                super().get_queryset().filter(categoria=CategoriePizza.PIZZE_SPECIALITA)
            )

    objects = Manager()


class PizzeSpecialiaBianche(Pizza):
    class Meta:
        proxy = True

    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return (
                super()
                .get_queryset()
                .filter(categoria=CategoriePizza.PIZZE_SPECIALI_BIANCHE)
            )

    objects = Manager()


class PizzeNovita(Pizza):
    class Meta:
        proxy = True

    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(categoria=CategoriePizza.PIZZE_NOVITA)

    objects = Manager()


class Bibita(models.Model):
    nome = models.CharField(default="", max_length=100)
    prezzo = models.FloatField(null=True)
    categoria = models.IntegerField(choices=CategorieBibita.choices)
    disponibile = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.nome} - {self.get_categoria_display()}"


class BibitaGrande(Bibita):
    class Meta:
        proxy = True

    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return (
                super().get_queryset().filter(categoria=CategorieBibita.BIBITA_GRANDE)
            )

    objects = Manager()


class BibitaPiccola(Bibita):
    class Meta:
        proxy = True

    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return (
                super().get_queryset().filter(categoria=CategorieBibita.BIBITA_PICCOLA)
            )

    objects = Manager()
