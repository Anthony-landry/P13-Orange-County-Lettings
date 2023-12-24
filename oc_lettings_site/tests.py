from django.test import TestCase
from django.urls import reverse

import pytest

from oc_lettings_site.views import error500


# flake8 --format=html --htmldir=flake-report  --exclude=venv

@pytest.mark.django_db
class TestProject(TestCase):
    r"""Class qui permet de tester les pages oc_lettings_site, et qui hérite de Testcase."""

    def test_renders_index(self):
        """Méthode qui test la page index.

        :param self: L'instance de TestProject
        :type self: TestProject
        .. note:: Cherche "Welcome to Holiday Homes", et, si trouvé, retourne le status 200.
        """

        response = self.client.get(reverse("index"))
        self.assertIn("Welcome to Holiday Homes", str(response.content))
        self.assertEqual(response.status_code, 200)

    def test_renders_404(self):
        r"""Méthode qui test si 404 est dans la page et le code de statut.

        :param self: L'instance de TestProject.
        :type self: TestProject
        .. note:: Test si 404 est bien retourné en 404 pour une page inexistante.
        """

        response = self.client.get("http://127.0.0.1:8000/bob")
        self.assertIn("404", str(response.content))
        self.assertEqual(response.status_code, 404)

    def test_renders_500(self):
        r"""Méthode qui test si 500 est dans la page.

        :param self: L'instance de TestProject
        :type self: TestProject

        .. note:: Test si le code de statut est bien retourné en 500 pour une
                  page d'erreur provenant du serveur.
        """
        response = self.client.get(reverse(error500))
        self.assertIn("500", str(response.content))
        self.assertEqual(response.status_code, 500)
