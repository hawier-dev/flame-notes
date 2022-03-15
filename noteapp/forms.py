from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=120,required=True,widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Title",
                "class": "uk-input default-radius",
            }
        ),
        label="",
    )
    description = forms.CharField(max_length=500,required=False,widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Description",
                "class": "uk-textarea default-radius",
            }
        ),
        label="",
    )

    class Meta:
        model = Note
        exclude = ("user", )