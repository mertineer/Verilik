from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms

# Create your views here.
class ServicesPage(TemplateView):
    template_name='services.html'

# class ContactPage(TemplateView):
#     template_name='contact.html'

class TeamPage(TemplateView):
    template_name='team.html'

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
    return render(request,'contact.html',{'form':form})
