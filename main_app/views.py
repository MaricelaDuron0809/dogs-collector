from django.shortcuts import render, redirect
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Dog, Treat, Pawll
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pawlls"] = Pawll.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"



class DogList(TemplateView):
    template_name = "dog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["dogs"] = Dog.objects.filter(name__icontains=name)
        
            context["header"] = f"Searching for {name}"
        else:
            context["dogs"] = Dog.objects.all()
            
            context["header"] = "The Best Doggos"
        return context
    
class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'img', 'bio', 'verified_dog']
    template_name = "dog_create.html"
    success_url = "/dogs/"

class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pawlls"] = Pawll.objects.all()
        return context
    
    
    
class DogUpdate(UpdateView):
    model = Dog
    fields = ['name', 'img', 'bio', 'verified_dog']
    template_name = "dog_update.html"
    
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})
   
class DogDelete(DeleteView):
    model = Dog
    template_name = "dog_delete_confirm.html"
    success_url = "/dogs/"  
    
class TreatCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        length = request.POST.get("length")
        dog = Dog.objects.get(pk=pk)
        Treat.objects.create(name=name, length=length, dog=dog)
        return redirect('dog_detail', pk=pk)
    
class PawllDogAssoc(View):

    def get(self, request, pk, dog_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Pawll.objects.get(pk=pk).dogs.remove(dog_pk)
        if assoc == "add":
            Pawll.objects.get(pk=pk).dogs.add(dog_pk)
        return redirect('home')
