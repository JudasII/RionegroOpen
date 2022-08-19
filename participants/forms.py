from pickle import FALSE
from django import forms

class participants(forms.Form):
    nombres = forms.CharField(label='nombres', max_length=50)
    apellidos = forms.CharField(label='apellidos', max_length=50)
    documento = forms.CharField(label= "documento")
    genero = forms.CharField(label="genero", max_length=50)
    academia = forms.CharField(label="academia",max_length=50)
    fechaNacimiento = forms.CharField(label="fechaNacimiento")
    cinturon = forms.CharField(label="cinturon",max_length=50)
    pais = forms.CharField(label = "pais",max_length=50)
    ciudad = forms.CharField(label="ciudad", max_length= 50)
    Categoria = forms.CharField(label="Categoria", max_length=50)
    filename = forms.ImageField()

class participantID(forms.Form):
    documento = forms.CharField(label= "documento")

