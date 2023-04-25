from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Atlet,Vykon,Uzivatel
from .forms import AtletForm,VykonForm,UzivatelForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
class AtletIndex(generic.ListView):
    template_name = "obludarium/atlet_index.html"
    context_object_name = "atleti"
#Třída která ztvárňuje html kod stránky atlet_index.html
    def get_queryset(self):
        return Atlet.objects.all().order_by("-id")
#Metoda pro zobrazení všech atletů podle jejich id

class CurrentAtletView(generic.DetailView):
    model= Atlet
    template_name= "obludarium/atlet_detail.html"
#Třída pro zobrazení detailu atleta

    def get(self,request,pk):
        try:
            atlet=self.get_object()

        except:
            return redirect("atleti_index")
        return render(request,self.template_name,{"atlet":atlet})

    def post(self,request,pk):
        if request.user.is_authenticated:
            if "edit" in request.POST:
                return redirect("edit_atlet",pk=self.get_object().pk)
            else:
                if not request.user.is_admin:
                    messages.info(request,"Nemáš práva pro smazání atleta.")
                    return redirect(reverse("atleti_index"))
                else:
                    self.get_object().delete()
        return redirect(reverse("atleti_index"))

class EditAtlet(LoginRequiredMixin,generic.edit.CreateView):
    form_class = AtletForm
    template_name = "obludarium/create_atlet.html"

    def get(self,request,pk):
        if not request.user.is_admin:
            messages.info(request,"Nemáš práva pro úpravu atleta.")
            return redirect(reverse("atleti_index"))
        try:
            atlet=Atlet.objects.get(pk=pk)
        except:
            messages.error(request, "Tento atlet neexistuje!")
            return redirect("atleti_index")
        form = self.form_class(instance=atlet)
        return render(request,self.template_name,{"form":form})

    def post(self,request,pk):
        if not request.user.is_admin:
            messages.info(request,"Nemáš práva pro úpravu atleta.")
            return redirect(reverse("atleti_index"))
        form = self.form_class(request.POST)
        if form.is_valid():
            jmeno = form.cleaned_data["jmeno"]
            prijmeni = form.cleaned_data["prijmeni"]
            vyska = form.cleaned_data["vyska"]
            vaha = form.cleaned_data["vaha"]
            sex = form.cleaned_data["sex"]
            procenta_tuku = form.cleaned_data["procenta_tuku"]
            tagy = form.cleaned_data["tagy"]
            try:
                atlet = Atlet.objects.get(pk = pk)
            except:
                messages.error(request,"Tento atlet neexistuje!")
                return redirect(reverse("atleti_index"))
            atlet.jmeno = jmeno
            atlet.prijmeni = prijmeni
            atlet.vyska = vyska
            atlet.vaha = vaha
            atlet.sex = sex
            atlet.procenta_tuku = procenta_tuku
            atlet.tagy.set(tagy)
            atlet.save()
        return redirect("atlet_detail",pk = atlet.id)
class CreateAtlet(generic.edit.CreateView):
    form_class = AtletForm
    template_name = "obludarium/create_atlet.html"
#Třída pro zobrazení stránky pro vytvoření nového atleta

#Metoda pro GET request, zobrazí pouze formulář
    def get(self,request):
        if not request.user.is_admin:
            messages.info(request,"Nemáš práva pro přidání atleta.")
            return redirect(reverse("atleti_index"))
        form= self.form_class(None)
        return render(request,self.template_name,{"form":form})

# Metoda pro POST request, zkontroluje formulář, pokud je validní vytvoří nového atleta, pokud ne
# zobrazí formulář s chybovou hláškou
    def post(self,request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro přidání atleta.")
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request,self.template_name,{"form":form})


class CreateVykon(generic.edit.CreateView):
    form_class = VykonForm
    template_name = "obludarium/create_vykon.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request, self.template_name, {"form": form})

class UzivatelViewRegister(generic.edit.CreateView):
    form_class = UzivatelForm
    model = Uzivatel
    template_name = "obludarium/user_form.html"

    def get(self,request):
        if request.user.is_authenticated:
            messages.info(request,"Už jsi přihlášený, nemůžeš se registrovat.")
            return redirect(reverse("atleti_index"))
        else:
            form = self.form_class(None)
        return render(request,self.template_name,{"form":form})
#Metoda get zobrazuje formulář (GET- dostaň formulář)
    def post(self,request):
        if request.user.is_authenticated:
            messages.info(request,"Už jsi přihlášený, nemůžeš se registrovat")
            return redirect(reverse("atleti_index"))
        form = self.form_class(request.POST)#zpracovává odeslaný formulář
        if form.is_valid(): #ověřuje validně vyplněno
            uzivatel = form.save(commit = False) #ukládá, ale necommituje protože budeme hashovat heslo
            password = form.cleaned_data["password"]
            uzivatel.set_password(password)
            uzivatel.save() #ukládá uživatele
            login(request,uzivatel) #přihlašuje uživatele
            return redirect("atleti_index")

        return render(request,self.template_name, {"form":form})
#Metoda POST jakoby POSTuje formulář- odesílá data a RENDER kombinuje HTML template a vyplněný form ve výsledný view

class UzivatelViewLogin(generic.edit.CreateView):
    form_class = LoginForm
    template_name = "obludarium/user_form.html"

    def get(self,request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se přihlásit znovu.")
            return redirect(reverse("atleti_index"))
        else:
            form = self.form_class(None)
        return render(request,self.template_name, {"form":form})

    def post(self,request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se přihlásit znovu.")
            return redirect(reverse("atleti_index"))
        form= self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user =authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect("atleti_index")
            else:
                messages.error(request, "Tento účet neexistuje.")
        return render(request,self.template_name,{"form":form})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        messages.info(request,"Nemůžeš se odhlásit, pokud nejsi přihlášený.")
    return redirect(reverse("login"))

def vykon_detail(request, atlet_id, vykon_id):
    atlet = get_object_or_404(Atlet, pk=atlet_id)
    vykon = get_object_or_404(Vykon, pk=vykon_id, atlet=atlet)
    context = {'atlet': atlet, 'vykon': vykon}
    return render(request, 'vykon_detail.html', context)

