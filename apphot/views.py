from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.db.models import Q
from django.views.generic import FormView
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    

class GenericIndex(FormView):
    template_name = 'contact.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def form_valid(self, form, *args, **kwargs):
        form.sendEmail()
        messages.success(self.request, _('E-mail enviado com sucesso !'))
        return super(GenericIndex, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar o e-mail'))
        return super(GenericIndex, self).form_invalid(form, *args, **kwargs)