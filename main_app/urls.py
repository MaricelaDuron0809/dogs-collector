from django.urls import path
from . import views


urlpatterns = [
path('', views.Home.as_view(), name="home"),
path('about/', views.About.as_view(), name="about"),
path('dogs/', views.DogList.as_view(), name="dog_list"),
path('dogs/new/', views.DogCreate.as_view(), name="dog_create"),
path('dogs/<int:pk>/', views.DogDetail.as_view(), name="dog_detail"),
path('dogs/<int:pk>/update',
         views.DogUpdate.as_view(), name="dog_update"),
path('dogs/<int:pk>/delete',
         views.DogDelete.as_view(), name="dog_delete"),
path('dogs/<int:pk>/treats/new/',
         views.TreatCreate.as_view(), name="treat_create"),
path('pawlls/<int:pk>/dogs/<int:dog_pk>/',
         views.PawllDogAssoc.as_view(), name="pawll_dog_assoc"),
path('accounts/signup/', views.Signup.as_view(), name="signup"),
 
]