from django.shortcuts import render, get_object_or_404
from .models import all_typs_imgs, image_store
from .forms import Image_from

# Create your views here.
def index(request):
    imgs = all_typs_imgs.objects.all()
    return render(request, 'website/all_index.html', {'imgs': imgs})

def img_detail(request, img_id):
    img = get_object_or_404(all_typs_imgs, pk=img_id)
    return render(request, 'website/img_detail.html', {'img': img})

def image_stores(request):
    ImageStores = None
    if request.method == 'POST':
        # Handle form submission if needed
        form = Image_from(request.POST)
        if form.is_valid():
            # Process the form data using changed_data; note that cleaned_data is usually preferred.
            imagetyps = form.cleaned_data['image_types']
            ImageStores = image_store.objects.filter(image_type=imagetyps)
    else:
        request.method == 'GET'
        form = Image_from()
    return render(request, 'website/image_stores.html', {'ImageStores': ImageStores, 'form': form})