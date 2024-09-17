from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import BungaForm
from main.models import Bunga

# Create your views here.
def show_main(request):
    bunga_entries = Bunga.objects.all()

    context = {
        'app_name' : 'floemin',
        'name': 'Nabila Maharani Putri',
        'class': 'PBP B',
        'bunga_entries' : bunga_entries
    }

    return render(request, "main.html", context)

def create_bunga_entry(request):
    form = BungaForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_bunga_entry.html", context)

def show_xml(request):
    data = Bunga.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Bunga.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Bunga.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Bunga.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")