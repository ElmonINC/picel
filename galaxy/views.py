# Create your views here.
# gallery/views.py

from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def index(request):
    return render(request, 'galaxy/index.html')

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galaxy')
    else:
        form = ImageForm()
    return render(request, 'galaxy/upload.html', {'form': form})

def galaxy(request):
    images = Image.objects.all()

    # Add absolute URL to each image manually
    image_data = []
    for image in images:
        full_url = request.build_absolute_uri(image.image.url)
        image_data.append({
            'image': image,
            'url': full_url
        })
    return render(request, 'galaxy/list.html', {'images': images})
