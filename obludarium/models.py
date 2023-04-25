from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Tag(models.Model):
    tag_title = models.CharField(max_length=30,verbose_name="Tagy")

    def __str__(self):
        return self.tag_title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tagy"


class Atlet(models.Model):
    jmeno= models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    vyska = models.IntegerField(null=True)
    vaha = models.IntegerField(null=True)
    sex = models.CharField(max_length=1)
    procenta_tuku= models.IntegerField(null=True)
    tagy = models.ManyToManyField(Tag)


    def __init__(self,*args,**kwargs):
        super(Atlet,self).__init__(*args,**kwargs)


    def __str__(self):
        tags = [i.tag_title for i in self.tagy.all()]
        return "Jméno: {0} | Prijmeni: {1} | Vyska: {2} | Vaha: {3} | Sex: {4} | Procenta tuku: {5} | Tagy: {6}".format(self.jmeno,self.prijmeni,self.vyska,self.vaha,self.sex,self.procenta_tuku,tags)

    class Meta:
        verbose_name="Atlet"
        verbose_name_plural= "Atleti"

class Vykon(models.Model):
    atlet= models.ForeignKey(Atlet,on_delete = models.CASCADE)
    push_ups= models.IntegerField(null=True)
    cmj = models.IntegerField(null=True)
    row_500= models.CharField(max_length=20)#bude potřeba převádět na int
    squat= models.IntegerField(null=True)

    def name(self):
        return self.atlet.atlet_id

    def __str__(self):
        return "Atlet: {0} | Push-ups: {1} | CMJ: {2} | Row 500m: {3} | Squat: {4}".format(self.atlet.jmeno,self.push_ups,self.cmj,self.row_500,self.squat)

    class Meta:
        verbose_name="Výkon"
        verbose_name_plural="Výkony"

class UzivatelManager(BaseUserManager):
    #Vytvoří uživatele
    def create_user(self,email,password):
        print(self.model)
        if email and password:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save
        return user
    #Vytvoří admina
    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_admin = True
        user.save()
        return user

class Uzivatel(AbstractBaseUser):
    email = models.EmailField(max_length = 300, unique=True)
    is_admin = models.BooleanField(default = False)

    class Meta:
        verbose_name = "uživatel"
        verbose_name_plural = "uživatelé"

    objects = UzivatelManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return "email: {}".format(self.email)
    @property
    def is_staff(self):
        return self.is_admin
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

