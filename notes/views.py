from django.http import HttpResponse
from .models import Note
from django.shortcuts import render

def index(request):
    all_notes = Note.objects.all().order_by("created_at")
    return render(request, 'notes/index.html', {'notes': all_notes})