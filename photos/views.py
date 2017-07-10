from django.shortcuts import render
from .models import Photo
# Create your views here.


def home(request):
    photos = Photo.objects.all()
    context_object = {
        'photos': photos
    }
    return render(request, 'photos/index.html', context=context_object)

