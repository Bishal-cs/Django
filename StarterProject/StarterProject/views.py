from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the StarterProject index.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world. You're at the StarterProject about.")

def contact(request):
    return HttpResponse("Hello, world. You're at the StarterProject Contact.")