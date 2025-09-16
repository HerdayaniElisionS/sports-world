from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

from main.forms import ProductForm
from main.models import Product

def show_main(request):
    products = Product.objects.all() 
    context = {
        'npm': '2406365313',     
        'name': 'Herdayani Elision Sitio',   
        'class': 'PBP KKI',       
        'products': products,
    }
    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_main')
    return render(request, "add_product.html", {'form': form})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {'product': product})

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    if not data.exists():
        return HttpResponse(status=404)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    try:
        obj = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    return HttpResponse(serializers.serialize("json", [obj]), content_type="application/json")
