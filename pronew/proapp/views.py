from django.shortcuts import render
from .models import*
from .form import*

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def data(request):
    s= Signin.objects.all()
    content={'data':s}
    return render(request,'data.html',content)
def form1(request):
    form= listform()
    if(request.method=='POST'):
        if form.is_valid():
            form.save
        return home(request)
    return render(request,'form.html',{'form':form})