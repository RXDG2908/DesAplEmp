from django.test import TestCase
from django.urls import reverse

from .models import Item


class ItemModelTest(TestCase):
    """Pruebas del modelo Item."""

    def test_str_devuelve_el_nombre(self):
        item = Item.objects.create(name='Teclado mecánico')
        self.assertEqual(str(item), 'Teclado mecánico')

    def test_created_at_se_asigna_automaticamente(self):
        item = Item.objects.create(name='Mouse inalámbrico')
        self.assertIsNotNone(item.created_at)

    def test_description_es_opcional(self):
        item = Item.objects.create(name='Cable HDMI')
        self.assertEqual(item.description, '')


class ItemListViewTest(TestCase):
    """Pruebas de la vista item_list."""

    def test_la_vista_responde_correctamente(self):
        respuesta = self.client.get(reverse('core:item_list'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'core/item_list.html')

    def test_muestra_los_items_registrados(self):
        Item.objects.create(name='Impresora láser', description='Área de ventas')
        respuesta = self.client.get(reverse('core:item_list'))
        self.assertContains(respuesta, 'Impresora láser')

    def test_mensaje_cuando_no_hay_items(self):
        respuesta = self.client.get(reverse('core:item_list'))
        self.assertContains(respuesta, 'No hay ítems registrados todavía.')
