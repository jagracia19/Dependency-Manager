from django.shortcuts import render
from .models import File

def index(request):
    files = File.objects.all()
    return render(request, 'index.html', {'files': files})
