from django import forms
from .models import Atlet,Vykon,Tag,Uzivatel

class AtletForm(forms.ModelForm):
    tagy=forms.ModelMultipleChoiceField(queryset= Tag.objects.all(),required = False)
    class Meta:
        model=Atlet
        fields=["jmeno","prijmeni","vyska","vaha","sex","procenta_tuku","tagy"]
    #Třída která registruje nového atleta(dědí z django forms)
class VykonForm(forms.ModelForm):
    class Meta:
        model=Vykon
        fields=["atlet","push_ups","cmj","row_500","squat"]
    #Třída která registruje nový výkon u libovolného atleta
class UzivatelForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Uzivatel
        fields = ["email","password"]
    #třída formuláře, která tvoří formulář(děděný z django frameworks) pro registraci nového uživatele
class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ["email","password"]
    #Třída formuláře, která umožňuje login uživateli