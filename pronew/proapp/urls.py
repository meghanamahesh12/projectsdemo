from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('data/',views.data,name='data'),
    path('form1/',views.form1,name='data'),
    
]
