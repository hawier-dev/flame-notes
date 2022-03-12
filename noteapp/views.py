from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import Note
from django.shortcuts import render
from .forms import NoteForm

def dashboard(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("flame_notes:dashboard")
    notes_list = Note.objects.all()
    form = NoteForm()
    return render(request, "base.html", {'notes_list': notes_list, "form": form})

def delete_post(request,post_id=None):
    post_to_delete=Note.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect("flame_notes:dashboard")