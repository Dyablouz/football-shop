from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
import datetime
from django.urls import reverse
from django.utils.html import strip_tags

@ensure_csrf_cookie
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406422986',
        'name': request.user.username,
        'class': 'PBP B',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)

@login_required(login_url='/login')
def add(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        new_product = form.save(commit = False)
        new_product.user = request.user
        new_product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add.html", context)

@login_required
@require_http_methods(["POST"])
def add_ajax(request):
    name = strip_tags(request.POST.get('name', '')).strip()
    description = strip_tags(request.POST.get('description', '')).strip()

    product = Product(
        name=name,
        description=description,
        price=request.POST.get('price') or 0,
        stock=request.POST.get('stock') or 0,
        thumbnail=request.POST.get('thumbnail') or '',
        category=request.POST.get('category') or '',
        is_featured=(request.POST.get('is_featured') in ['on','true','1']),
        user=request.user,
    )
    product.save()

    data = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'stock': product.stock,
        'description': product.description,
        'thumbnail': product.thumbnail,
        'category': product.category,
        'is_featured': product.is_featured,
        'user_id': product.user_id,
    }
    return JsonResponse(data, status=201)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit.html", context)

@login_required
@require_http_methods(["POST", "PUT", "PATCH"])
def update_product_ajax(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

    if 'name' not in request.POST:
        return HttpResponseBadRequest("Invalid payload")

    product.name = strip_tags(request.POST.get('name', product.name)).strip()
    product.description = strip_tags(request.POST.get('description', product.description)).strip()
    if 'price' in request.POST: product.price = request.POST.get('price') or product.price
    if 'stock' in request.POST: product.stock = request.POST.get('stock') or product.stock
    if 'thumbnail' in request.POST: product.thumbnail = request.POST.get('thumbnail') or product.thumbnail
    if 'category' in request.POST: product.category = request.POST.get('category') or product.category
    if 'is_featured' in request.POST:
        product.is_featured = (request.POST.get('is_featured') in ['on','true','1'])
    product.save()

    data = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'stock': product.stock,
        'description': product.description,
        'thumbnail': product.thumbnail,
        'category': product.category,
        'is_featured': product.is_featured,
        'user_id': product.user_id,
    }
    return JsonResponse(data)

def detail(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "detail.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required
@require_http_methods(["POST", "DELETE"])
def delete_product_ajax(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    product.delete()
    return HttpResponse(status=204)

# def show_json(request):
#     product_list = Product.objects.all()
#     json_data = serializers.serialize("json", product_list)
#     return HttpResponse(json_data, content_type="application/json")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id' : product.id,
            'name': product.name,
            'price': product.price,
            'stock' : product.stock,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
   try:
       product = Product.objects.get(pk=product_id)
       xml_data = serializers.serialize("xml", [product])
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

# def show_json_by_id(request, product_id):
#    try:
#        product = Product.objects.get(pk=product_id)
#        json_data = serializers.serialize("json", [product])
#        return HttpResponse(json_data, content_type="application/json")
#    except Product.DoesNotExist:
#        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'stock' : product.stock,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
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

@require_http_methods(["POST"])
def register_ajax(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return JsonResponse({"ok": True})
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

@require_http_methods(["POST"])
def login_ajax(request):
    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        resp = JsonResponse({"ok": True, "username": user.username})
        resp.set_cookie("last_login", str(datetime.datetime.now()))
        return resp
    return JsonResponse({"ok": False, "detail": "Invalid credentials"}, status=400)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@require_http_methods(["POST"])
def logout_ajax(request):
    logout(request)
    resp = JsonResponse({"ok": True})
    resp.delete_cookie("last_login")
    return resp
