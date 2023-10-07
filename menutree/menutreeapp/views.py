from django.shortcuts import render

def menu_view(request, menu_name):
    return render(request, 'menutree/menu_view.html', {'menu_name': menu_name})
