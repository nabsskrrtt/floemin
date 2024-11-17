from django.forms import ModelForm
from main.models import Bunga
from django.utils.html import strip_tags

class BungaForm (ModelForm):
    class Meta:
        model = Bunga
        fields = ["name", "price", "description", "stocks", "img_url"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_img_url(self):
        img_url = self.cleaned_data["img_url"]
        return strip_tags(img_url)