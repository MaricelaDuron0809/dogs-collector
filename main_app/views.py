from django.shortcuts import render, redirect, reverse
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Dog, Treat, Pawll
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pawlls"] = Pawll.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"


@method_decorator(login_required, name='dispatch')
class DogList(TemplateView):
    template_name = "dog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["dogs"] = Dog.objects.filter(name__icontains=name, user=self.request.user)
        
            context["header"] = f"Searching for {name}"
        else:
            context["dogs"] = Dog.objects.filter(user=self.request.user)
            
            context["header"] = "The Best Doggos"
        return context
    
@method_decorator(login_required, name='dispatch')
class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'img', 'bio', 'verified_dog']
    template_name = "dog_create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DogCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('dog_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pawlls"] = Pawll.objects.all()
        return context
    
    
@method_decorator(login_required, name='dispatch')
class DogUpdate(UpdateView):
    model = Dog
    fields = ['name', 'img', 'bio', 'verified_dog']
    template_name = "dog_update.html"
    
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})
@method_decorator(login_required, name='dispatch')
class DogDelete(DeleteView):
    model = Dog
    template_name = "dog_delete_confirm.html"
    success_url = "/dogs/"  
@method_decorator(login_required, name='dispatch')    
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

class Signup(View):
   
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
  
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dog_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)