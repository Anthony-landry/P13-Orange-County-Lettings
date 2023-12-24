import pytest
from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db
class TestLettings(TestCase):
    r"""Class qui permet de tester les pages lettings, et qui hérite de ``Testcase``."""

    def test_lettings_index(self):
        r"""Test si la page d'index s'affiche correctement.
         On vérifie si le titre est dans la page et retourne un status 200

        :param self: L'instance de TestLettings
        :type: TestLettings
        """
        response = self.client.get(reverse("lettings:index"))
        self.assertIn("Lettings", str(response.content))
        self.assertEqual(response.status_code, 200)

    def test_letting_page(self):
        r"""Test l'affichage spécifique d'un page letting,
        avec la creation d'une adresse et d'un letting.

        :param self: L'instance de TestLettings.
        :type self: TestLettings

        .. note:: La vérification du titre et adresse de lettings correspond à
                  celui attendu sur la page.
        """
        address = Address.objects.create(
            number="1",
            street="street",
            city="city",
            state="state",
            zip_code="000000",
            country_iso_code="XXX"
        )
        letting = Letting.objects.create(
            title="title",
            address=address
        )
        response = self.client.get(reverse("lettings:letting", kwargs={"letting_id": 1}))
        self.assertIn(letting.title, str(response.content))
        self.assertEqual(response.status_code, 200)

    def test_create_letting_with_valid_address(self):
        r"""Test la creation de letting avec une adresse valide.

        :param self: L'instance de TestLettings.
        :type self: TestLettings
        """
        address = Address.objects.create(number=123, street="Main St",
                                         city="City", state="NY", zip_code=12345,
                                         country_iso_code="USA")
        letting = Letting(title="Test Letting", address=address)
        self.assertEqual(letting.title, "Test Letting")
        self.assertEqual(letting.address, address)

    def test_create_letting_with_invalid_address(self):
        r"""Test la creation de letting avec une adresse non valide.

        :param self: L'instance de TestLettings.
        :type self: TestLettings
        """
        try:
            Address.objects.create(number=123, street="Main St",
                                   city="City", state="NY", zip_code=-2,
                                   country_iso_code="USA")
        except Exception as error:
            print(error)
            self.assertEqual(str(error), "CHECK constraint failed: zip_code")

    def testSTR(self):
        r"""Test la représentation en chaine d'un objet Address.

        :param self: L'instance de TestLettings.
        :type self: TestLettings
        """
        address = Address.objects.create(number=123, street="Main St",
                                         city="City", state="NY", zip_code=2,
                                         country_iso_code="USA")
        self.assertEqual(str(address), "123 Main St")
