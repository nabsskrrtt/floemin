from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'floemin',
        'name': 'Nabila Maharani Putri',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)