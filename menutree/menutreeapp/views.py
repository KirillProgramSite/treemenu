from django.shortcuts import render
from menutreeapp.models import MenuItem

# Create your views here.
def index(request):
    menu = MenuItem.objects.all()
    context = {
        "menu": menu

    }

    print(context)

    return render(request, 'index.html', context=context)