""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from django.forms import ModelForm
from django import forms
from .models import Post




""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class PostFormCreate(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo' , 'contenido' , 'categoria']
        labels = { "categoria" : ("Categoria")}
        widgets = {
            "titulo" : forms.TextInput(attrs={ "class" : 'form-control'}),
            "contenido" : forms.Textarea(attrs={ "class" : 'form-control', "rows" : 5}),
            "categoria" : forms.Select(attrs={ "class" : 'form-control'}),
        }
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
