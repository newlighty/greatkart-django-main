from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request, 'home.html', context)



    def home(request):
     output = _("خوش امدید")
    
    return render(output, 'home.html', context)
