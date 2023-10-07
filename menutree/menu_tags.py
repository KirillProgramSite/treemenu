from django import template
from .models import MenuItem

register = template.Library()


@register.inclusion_tag('menutree/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return {'menu_items': menu_items, 'request': request, 'menu_name': menu_name}
