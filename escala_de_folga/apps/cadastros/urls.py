
from django.urls import path
from .views import *

urlpatterns = [
    path('medicos/', MedicoListView.as_view(), name='list-medicos'),
    path('medicos/create/', create_medico, name='create-medico'),
    path('medicos/<id>/update/', update_medico, name='update-medico'),

    path('postos/', PostoListView.as_view(), name='list-postos'),
    path('postos/create/', create_posto, name='create-posto'),
    path('postos/<id>/update/', update_posto, name='update-posto'),

    path('folgas/', FolgaListView.as_view(), name='list-folgas'),
    path('folgas/create/', create_folga, name='create-folga'),
    path('folgas/<id>/update/', update_folga, name='update-folga'),
]
