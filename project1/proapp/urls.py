from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('page1/',views.home,name='home'),
    
]
