from django.forms import ModelForm
from main.models import Bunga

class BungaForm (ModelForm):
    class Meta:
        model = Bunga
        fields = ["name", "price", "description", "stocks", "img_url"]