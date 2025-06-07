from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import all_typs_imgs

# Create your views here.
def index(request):
    imgs = all_typs_imgs.objects.all()
    return render(request, 'website/all_index.html', {'imgs': imgs})

def img_detail(request, img_id):
    img = get_object_or_404(all_typs_imgs, pk=img_id)
    return render(request, 'website/img_detail.html', {'img': img})