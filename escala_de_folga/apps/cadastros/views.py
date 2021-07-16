from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView

from .models import *
from .forms import *


class CustomListView(ListView):
    template_name = "list_model.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name_plural+' cadastrados:'
        return context


def create_model(request, model_form_class: type, success_url):
    context = {}

    form = model_form_class(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(success_url)

    context['form'] = form
    return render(request, "create_model.html", context)


def update_model(request, id, model_class: type, model_form_class: type, success_url):
    context = {}

    object = get_object_or_404(model_class, id=id)

    form = model_form_class(request.POST or None, instance=object)

    if form.is_valid():
        form.save()
        return redirect(success_url)

    context["form"] = form
    return render(request, "update_model.html", context)


# Médico
class MedicoListView(CustomListView):
    model = Medico

def create_medico(request):
    return create_model(request, MedicoForm, 'list-medicos')

def update_medico(request, id):
    return update_model(request, id, Medico, MedicoForm, 'list-medicos')


# Posto
class PostoListView(CustomListView):
    model = Posto

def create_posto(request):
    return create_model(request, PostoForm, 'list-postos')

def update_posto(request, id):
    return update_model(request, id, Posto, PostoForm, 'list-postos')

# Folga
class FolgaListView(CustomListView):
    model = Folga

def create_folga(request):
    return create_model(request, FolgaForm, 'list-folga')

def update_folga(request, id):
    return update_model(request, id, Folga, FolgaForm, 'list-folgas')
