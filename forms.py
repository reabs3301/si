from http import client
from django.db.models import fields
from django import forms
from .models import centre_pv, emprunt, fournisseur, matiere_premiere, produit, pvs, team, client, vente

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

class pvform(forms.ModelForm):
    class Meta:
        model = pvs
        fields = "__all__"

class venteform(forms.ModelForm):
    class Meta:
        model = vente
        fields = ["time","client_achter","produit","qte","prix","payement_faciliter"]

class PointageForm(forms.Form):
    employer_Present = forms.BooleanField(required=False, initial=False)
    #employer_absent = forms.BooleanField(required=False, initial=False)


class empruntform(forms.ModelForm):
    class Meta:
        model = emprunt
        fields = "__all__"
