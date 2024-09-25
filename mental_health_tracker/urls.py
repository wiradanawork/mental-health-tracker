from django.urls import path, include
from main.views import show_main
from main.views import delete_mood

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('', include('main.urls')),
]