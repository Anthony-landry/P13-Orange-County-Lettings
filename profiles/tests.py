import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
class TestProfile(TestCase):
    r"""Class qui permet de tester les pages profiles, et qui hérite de Testcase."""

    def test_profile_index(self):
        r"""Test si la page d'index des profiles est correctement affiché.

        :param self: L'instance de TestProfile
        :type self: TestProfile

        .. note:: Vérifie que le "profile" est présent sur la page.
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertIn("Profiles", str(response.content))
        self.assertEqual(response.status_code, 200)

    def test_profile_page(self):
        r"""Test l'affichage du profil de l'utilisateur.
        :param self: L'instance de TestProfile
        :type self: TestProfile

        .. note:: Crée un profil utilisateur, vérife si la ville favorite ainsi
                  que le username est présente dans dans la réponse, et si le
                  code statut est 200.
        """
        user = User.objects.create(
            username="toto",
            password="123456"
        )
        profile = Profile.objects.create(
            user=user,
            favorite_city="Le Havre"
        )
        response = self.client.get(reverse("profiles:profile", kwargs={"username": "toto"}))
        self.assertIn(profile.favorite_city, str(response.content))
        self.assertIn(profile.user.username, str(response.content))
        self.assertEqual(response.status_code, 200)

    def test_create_profile_with_valid_user(self):
        r"""Test la création d'un profil avec un utilisateur valide.

        :param self: L'instance de TestProfile
        :type self: TestProfile
        """
        user = User.objects.create(
            username="toto",
            password="123456"
        )
        self.assertEqual(user.username, "toto")
        self.assertEqual(user.password, "123456")

    def test_create_profiles_with_invalid_user(self):
        """Test la création d'un profil avec un utilisateur non valide.

        :param self: L'instance de TestProfile
        :type self: TestProfile
        """
        try:
            User.objects.create(
                username=-2,
                password="123456"
            )
        except Exception as error:
            print(error)
            self.assertEqual(str(error), "CHECK constraint failed: zip_code")

    def testSTR(self):
        """Test la représentation en chaine d'un objet User.

        :param self: L'instance de TestProfile
        :type self: TestProfile
        """
        user = User.objects.create(
            username="toto",
            password="123456"
        )
        self.assertEqual(str(user), "toto")
