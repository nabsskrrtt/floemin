from django.urls import path
from main.views import show_main
from main.views import create_bunga_entry
from main.views import show_xml
from main.views import show_json
from main.views import show_xml_by_id
from main.views import show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-bunga-entry', create_bunga_entry, name='create_bunga_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]