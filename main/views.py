import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from main.forms import BungaForm
from main.models import Bunga
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    # bunga_entries = Bunga.objects.filter(user=request.user)

    context = {
        'app_name' : 'floemin',
        'name': request.user.username,
        'class': 'PBP B',
        # 'bunga_entries' : bunga_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_bunga_entry(request):
    form = BungaForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        bunga_entry = form.save(commit=False)
        bunga_entry.user = request.user
        bunga_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_bunga_entry.html", context)

def show_xml(request):
    data = Bunga.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Bunga.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Bunga.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Bunga.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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
        return response

   else:
      messages.error(request, "Invalid username or password. Please try again.")
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_bunga(request, id):
    # Get bunga entry berdasarkan id
    bunga = Bunga.objects.get(pk = id)

    # Set bunga entry sebagai instance dari form
    form = BungaForm(request.POST or None, instance=bunga)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_bunga.html", context)

def delete_bunga(request, id):
    # Get bunga berdasarkan id
    bunga = Bunga.objects.get(pk = id)
    # Hapus bunga
    bunga.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_flower_entry_ajax(request):
    bunga = strip_tags(request.POST.get("flower")) # strip HTML tags!
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description")) # strip HTML tags!
    stocks = request.POST.get("stocks")
    img_url = request.POST.get("img_url")
    user = request.user

    new_bunga = Bunga(
        bunga=bunga, price=price,
        description=description,
        stocks=stocks, img_url=img_url,
        user=user
    )
    new_bunga.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_flower_flutter(request):
    print(request.method)
    if request.method == 'POST':

        data = json.loads(request.body)
        print(data)
        new_flower = Bunga.objects.create(
            user=request.user,
            name=data["bunga"],
            description=data["description"],
            price=int(data["price"]),
            stocks=int(data["stocks"]),
            img_url=data["img_url"]
        )

        new_flower.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)