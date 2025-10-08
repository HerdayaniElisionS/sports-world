from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from .models import Product


from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.utils.html import strip_tags
from django.contrib import messages



@login_required(login_url='/login')
def show_main(request):
    context = {
        'npm': '2406365313',
        'name': request.user.username,
        'class': 'PBP KKI',
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def product_detail(request, id):
    get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {'product_id': id})


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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            
            return redirect('main:login')
    context = {'form':form}

    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
          user = form.get_user()
          login(request, user)
          response = HttpResponseRedirect(reverse("main:show_main"))
          response.set_cookie('last_login', str(datetime.datetime.now()))
          messages.success(request, 'Login successful!')
          return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    messages.success(request, 'You have logged out successfully.')
    return response

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': product
    }
    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product_list.html')

@require_GET
@login_required(login_url='/login')
def product_detail_json(request, id):
    p = get_object_or_404(Product, pk=id)
    data = {
        "id": str(p.id),
        "name": p.name,
        "description": p.description,
        "price": float(getattr(p, "price", 0)) if hasattr(p, "price") and getattr(p, "price", None) is not None else None,
        "stock": int(getattr(p, "stock", 0)) if hasattr(p, "stock") and getattr(p, "stock", None) is not None else None,
        "image_url": getattr(p, "image_url", "") if hasattr(p, "image_url") else "",
        "created_at": p.created_at.isoformat() if getattr(p, "created_at", None) else None,
        "user_id": getattr(p, "user_id", None),
    }
    return JsonResponse(data)

@require_GET
@login_required(login_url='/login')
def product_list_json(request):
    qs = Product.objects.all().order_by("-id")
    data = [
        {
            "id": str(p.id),
            "name": p.name,
            "description": p.description,
            "price": float(getattr(p, "price", 0)) if hasattr(p, "price") and getattr(p, "price", None) is not None else None,
            "stock": int(getattr(p, "stock", 0)) if hasattr(p, "stock") and getattr(p, "stock", None) is not None else None,
            "image_url": getattr(p, "image_url", "") if hasattr(p, "image_url") else "",
            "created_at": p.created_at.isoformat() if getattr(p, "created_at", None) else None,
            "user_id": getattr(p, "user_id", None),
        }
        for p in qs
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def add_product_entry_ajax(request):
    name = strip_tags((request.POST.get("name") or "").strip())
    description = strip_tags((request.POST.get("description") or "").strip())
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    image_url = request.POST.get("image_url", "").strip()

    if not name:
        return HttpResponseBadRequest("Name is required")

    product = Product(
        name=name,
        description=description,
    )

    if hasattr(product, "user"):
        product.user = request.user

    if hasattr(product, "price") and price not in (None, ""):
        try:
            product.price = float(price)
        except ValueError:
            return HttpResponseBadRequest("Invalid price")

    if hasattr(product, "stock") and stock not in (None, ""):
        try:
            product.stock = int(stock)
        except ValueError:
            return HttpResponseBadRequest("Invalid stock")

    if hasattr(product, "image_url"):
        product.image_url = image_url

    product.save()
    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def update_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)

    

    name = request.POST.get("name")
    description = request.POST.get("description")
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    image_url = request.POST.get("image_url")

    if name is not None:
        product.name = strip_tags(name.strip())
    if description is not None:
        product.description = strip_tags(description.strip())
    if price is not None and hasattr(product, "price"):
        try:
            product.price = float(price)
        except ValueError:
            return HttpResponseBadRequest("Invalid price")
    if stock is not None and hasattr(product, "stock"):
        try:
            product.stock = int(stock)
        except ValueError:
            return HttpResponseBadRequest("Invalid stock")
    if image_url is not None and hasattr(product, "image_url"):
        product.image_url = image_url.strip()

    product.save()
    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def delete_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if hasattr(product, "user_id") and product.user_id and product.user_id != request.user.id:
        return HttpResponse(status=403)
    product.delete()
    return HttpResponse(b"DELETED", status=200)

@csrf_exempt
@require_POST
def login_user_ajax(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return JsonResponse({"status": "OK", "redirect_url": reverse("main:show_main")}, status=200)
    return JsonResponse({"status": "ERROR", "errors": form.errors}, status=400)

@csrf_exempt
@require_POST
def register_user_ajax(request):
    post = request.POST.copy()
    if "username" in post:
        post["username"] = strip_tags(post["username"]).strip()
    if "email" in post:
        post["email"] = strip_tags(post["email"]).strip()

    form = UserCreationForm(post)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": "OK", "redirect_url": reverse("main:login")}, status=201)
    return JsonResponse({"status": "ERROR", "errors": form.errors}, status=400)