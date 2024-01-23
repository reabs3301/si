from django.db import models


# Create your models here.

class produit(models.Model) :
    prod_ID = models.AutoField(primary_key = True)
    prod_NAME = models.CharField(max_length = 30)
    price = models.FloatField()
    produced_at = models.DateTimeField(auto_now=True)
    prix_transfert = models.FloatField(default = 0)

class main_store(models.Model) :
    main_store_ID = models.AutoField(primary_key = True)
    main_store_NAME = models.CharField(max_length = 30)
    total_chiffre = models.FloatField()


class centre_pv(models.Model) : 
    centre_ID = models.AutoField(primary_key = True)
    centre_NAME = models.CharField(max_length = 30)
    centre_TEL = models.CharField(max_length = 10)
    centre_MAIL = models.EmailField()
    recette = models.FloatField()
    superior = models.ForeignKey(main_store , on_delete = models.CASCADE)
    
    #superior -> main_store_ID


class pvs(models.Model) :
    pv_val = models.TextField()
    concerned_center = models.ForeignKey(centre_pv , on_delete = models.CASCADE)


class client(models.Model) :
    client_ID = models.AutoField(primary_key = True)
    client_NAME = models.CharField(max_length = 30)
    client_ADR = models.CharField(max_length = 30)
    client_TEL = models.CharField(max_length = 10)
    client_POINT = models.IntegerField()

class agent(models.Model) : 
    agent_CODE = models.AutoField(primary_key = True)
    agent_NAME = models.CharField(max_length = 30)
    agent_PRENOM = models.CharField(max_length = 30)
    agent_TEL = models.CharField(max_length = 10)
    agent_SALAIRE_JR = models.FloatField()
    work = models.ForeignKey(main_store , on_delete = models.CASCADE)

class team(models.Model):
    employer_CODE = models.AutoField(primary_key=True)
    employer_NOM = models.CharField(max_length=30)
    employer_ADR = models.CharField(max_length=30)
    employer_TEL = models.CharField(max_length=10)
    employer_SALAIRE_JR = models.FloatField()
    centre_pnv = models.ForeignKey(centre_pv, on_delete=models.CASCADE)

class matiere_premiere(models.Model):
    matiere_ID = models.AutoField(primary_key=True)
    matiere_NAME = models.CharField(max_length=30)
    matiere_PRICE = models.FloatField()
    agent = models.ForeignKey(agent, on_delete=models.CASCADE)

class fournisseur(models.Model):
    fournisseur_ID = models.AutoField(primary_key=True)
    fournisseur_NAME = models.CharField(max_length=30)
    fournisseur_ADR = models.CharField(max_length=30)
    fournisseur_MAIL = models.EmailField()
    fournisseur_SOLD = models.FloatField()

class delivrer(models.Model):
    fournisseur = models.ForeignKey(fournisseur, on_delete=models.CASCADE)
    matiere_premiere = models.ForeignKey(matiere_premiere, on_delete=models.CASCADE) 


class secompose(models.Model):
    produit = models.ForeignKey(produit, on_delete=models.CASCADE)
    component = models.ForeignKey(matiere_premiere, on_delete=models.CASCADE)
    #component -> matiere_premiere

class R1(models.Model):
    produit_exist = models.ForeignKey(produit, on_delete=models.CASCADE)
    centre_pnv = models.ForeignKey(centre_pv, on_delete=models.CASCADE)
    QTE = models.IntegerField()
    #produit_exist -> id de produit , qte -> sa quantite


#look
class R2(models.Model):
    main_store = models.ForeignKey(main_store, on_delete=models.CASCADE)
    client_main_store = models.ForeignKey(client, on_delete=models.CASCADE)
    #place where client bought

#look
class R3(models.Model):
    client_centre = models.ForeignKey(client, on_delete=models.CASCADE)
    centre_pnv = models.ForeignKey(centre_pv, on_delete=models.CASCADE)
    #place where client bought 


class vente(models.Model):
    time = models.DateField()
    client_achter = models.ForeignKey(client , on_delete = models.CASCADE )
    produit = models.ForeignKey(produit, on_delete = models.CASCADE)
    qte = models.IntegerField()
    prix = models.FloatField()
    payement_faciliter = models.BooleanField()
    rest_total = models.FloatField(default = 0.0)
    saled_at =models.ForeignKey(centre_pv ,on_delete=models.CASCADE , default =  '')

class emprunt(models.Model):
    employe = models.ForeignKey(team, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now = True)
    somme = models.FloatField()
    
