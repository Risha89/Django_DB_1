from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Phone


def catalog(request):
    if 'sort' in request.GET:
        if request.GET['sort'] == 'name':
            phone_objects = Phone.objects.order_by('name')
        elif request.GET['sort'] == 'min':
            phone_objects = Phone.objects.order_by('price')
        elif request.GET['sort'] == 'max':
            phone_objects = Phone.objects.order_by('-price')

    else:
        phone_objects = Phone.objects.all()
    template = 'catalog.html'
    context = {'price': phone_objects}
    return render(request, template, context)

def show_product(request, slug):
    phone_objects = Phone.objects.filter(slug=f"{slug}")

    template = 'product.html'
    context = {'data': phone_objects}
    return render(request, template, context)

