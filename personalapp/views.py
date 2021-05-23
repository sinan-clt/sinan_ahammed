from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sinan(request):
    return render(request,'personal.html')