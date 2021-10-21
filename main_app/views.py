from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


from .models import Dog
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

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