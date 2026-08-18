from django.shortcuts import render

from .models import Item


def item_list(request):
    """Obtiene todos los ítems y los envía a la plantilla."""
    items = Item.objects.all()
    return render(request, 'core/item_list.html', {'items': items})
