from django.shortcuts import render
from .models import UploadedImage
from .forms import UploadImageForm
from ss_app.models import Photos

# Create your views here.

def home(request):
    photos = Photos.objects.all().order_by('sort_order')
    # photos = Photos.objects.get(pk=1)
    context = {             "allphotos": photos        }
    # context = { 'caption' : "Test me", 'when_where' : "wtf" }
    
    
    return render(request, "ss_app/home.html", context)
    
    

def upload_image(request):
    print("\n\n\n DEBUG : INSIDE OF upload_image \n\n\n")
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadImageForm()
    images = UploadedImage.objects.all()
    return render(request, 'ss_app/upload_image.html', {'form': form, 'images': images})