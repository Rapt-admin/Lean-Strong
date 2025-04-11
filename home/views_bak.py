from django.shortcuts import render

# Create your views here.
def show(request):
  return render(request,'index.html')  

def about_us(request):
  return render(request,'about.html')  
