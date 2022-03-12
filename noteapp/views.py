from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from django.shortcuts import render

def dashboard(request):
    notes_list = Note.objects.all()
    return render(request, "base.html", {'notes_list': notes_list})
def create(request):
    return render(request, "new_note.html")