from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    r"""Class qui representant une adresse physique."""

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    r"""Le numéro de rue doit être positif, limité à 4 chiffres (``PositiveIntegerField``)."""

    street = models.CharField(max_length=64)
    r"""Le numero de rue, est une chaine de caractère limitée à 64 caractères (``CharField``)."""

    city = models.CharField(max_length=64)
    r"""Le nom de la ville, est une chaine de caractère limitée à 64 caractères (``CharField``)."""

    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    r"""Region, est une chaine de caractère limitée à 2 caractères max et min (``CharField``)."""

    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    r"""Code postal, doit être positif et limité à 5 chiffres (``PositiveIntegerField``)."""

    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])
    r"""Initiale du pays, limitée à 3 lettre (``CharField``)."""

    class Meta:
        r"""Class qui permet de gérer le pluriel du model Address."""
        verbose_name_plural = 'addresses'

    def __str__(self):
        r"""Methode qui permet de gérer l'affichage d'une instance Adresse.

        :param self: l'instance du Address.
        :type self: Address
        :return: Le numéro suivant la rue.
        :rtype: str
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    r"""Classe qui hérite de models.model."""

    title = models.CharField(max_length=256)
    r"""Une chaine de caractère limitée à 256 caractères (``CharField``)."""

    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    r"""Une référence à la adresse associé (``OneToOneField``)."""

    def __str__(self):
        r"""Methode qui permet de gérer l'affichage d'une instance Letting.

        :param self: l'instance du Letting.
        :type self: Letting
        :return: Retourne un titre.
        :rtype: str
        """
        return self.title
