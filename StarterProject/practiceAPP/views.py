from django.shortcuts import render
from .models import all_typs_imgs

# Create your views here.
def index(request):
    imgs = all_typs_imgs.objects.all()
    return render(request, 'website/all_index.html', {'imgs': imgs})