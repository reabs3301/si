from http import client
from django.db.models import fields
from django import forms
from .models import centre_pv, fournisseur, matiere_premiere, produit, team, client

class productform(forms.ModelForm):
    class Meta:
        model = produit
        fields="__all__"

class centerform(forms.ModelForm):
    class Meta:
        model = centre_pv
        fields="__all__"        


class clientform(forms.ModelForm):
    class Meta:
        model = client
        fields="__all__"        

class fournisseurform(forms.ModelForm):
    class Meta:
        model = fournisseur
        fields="__all__"        


class matiereform(forms.ModelForm):
    class Meta:
        model = matiere_premiere
        fields="__all__"        


class teamform(forms.ModelForm):
    class Meta:
        model = team
        fields="__all__"        
