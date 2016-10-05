from django.core.urlresolvers import resolve
from django.test import TestCase
from lesTaches.views import home

class HomePageTestContent(TestCase):

    '''Test unitaire bidon'''
    def test_concatene(self):
        self.assertEqual("Bon"+"jour", "Bonjour")

    '''Test unitaire de la page accueil sur la racine du projet'''
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
