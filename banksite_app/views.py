from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView

from .models import Branch, Person
from .forms import PersonCreationForm


# Create your views here.
def Home(request):
    return render(request, 'home.html')


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Your application has been accepted")
            return redirect('person_add')
    return render(request, 'persons.html', {'form': form})

class UserDetailView(View):
    def get(self,request,*args,**kwargs):
        ab=Person.objects.all()
        return render(request,"person_list.html",{'persons':ab})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons.html', {'form': form})


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})
