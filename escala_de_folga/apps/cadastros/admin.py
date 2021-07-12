from .models import Escala, Medico, Posto
from django.contrib import admin

admin.site.register([Medico, Posto, Escala])
