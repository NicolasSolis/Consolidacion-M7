from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create (
            nombre='Laboratorio de Prueba',
            ciudad='Ciudad de Prueba',
            pais='País de Prueba'
        )

    def test_datos_laboratorio(self):
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        
        self.assertEqual(laboratorio.nombre, 'Laboratorio de Prueba')
        self.assertEqual(laboratorio.ciudad, 'Ciudad de Prueba')
        self.assertEqual(laboratorio.pais, 'País de Prueba')

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/laboratorio/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("insertar-lab"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse("insertar-lab"))
        self.assertTemplateUsed(response, "insertar.html")