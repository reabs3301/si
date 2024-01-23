from django.http import HttpResponse
from django.shortcuts import  get_object_or_404, redirect, render
from .models import centre_pv, fournisseur, produit, client, pvs, team, matiere_premiere , vente
from .forms import  PointageForm, centerform, clientform, empruntform, fournisseurform, matiereform, productform, pvform, teamform , pvs, venteform
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Create your views here.
 
def choosing(request):
    return render(request,'adding_home.html')
    
def afficher_table(request) :
    produits = produit.objects.all()
    centre = centre_pv.objects.all()
    clients = client.objects.all()
    fournisseurs = fournisseur.objects.all()
    employe = team.objects.all()
    matiere = matiere_premiere.objects.all()

    types={"produit":produits,
           "centre":centre,
           "client":clients,
           "fournisseur":fournisseurs,
           "team":employe,
           "matiere_premiere":matiere
          }


    return render(request,"index.html",types)


def afficher_produit(request , id) :
    produits = produit.objects.all()

    types={"produit":produits , 'id':id}

    return render(request,"select_produits.html",types)


def select(request , id , type) :
   
    types = {}

    if type == 'produit' :
        produits = produit.objects.get(prod_ID = id)
        types = {'produit' : produits}

    if type == 'centre' :
        centres = centre_pv.objects.get(centre_ID = id)
        types = {'centre' : centres }



    if type == 'client' :
        clients = client.objects.get(client_ID = id)
        types = {'client' : clients}

    if type == 'fournisseur' :    
        fournisseurs = fournisseur.objects.get(fournisseur_ID = id)
        types = {'fournisseur' : fournisseurs}


    if type == 'team' :
        employe = team.objects.get(employer_CODE = id)
        types = {'team' : employe}
        afficher_team(request,id)

    if type == 'matiere_premiere' :    
        matiere = matiere_premiere.objects.get(matiere_ID = id)
        types = {'matiere_premiere' : matiere}

    return render(request,"select.html",types)


def add_product(request,type):

    if type == 'produit' :    
        if request.method == 'POST':
            form = productform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = productform()  # Create a new empty form
                write = "Product added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = productform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})

    if type == 'center' :
        if request.method == 'POST':
            form = centerform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = centerform()  # Create a new empty form
                write = "centre added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = centerform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})
        return render(request, 'add.html', {'form': form})
    
    if type == 'pv' :
        if request.method == 'POST':
            form = pvform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = pvform()  # Create a new empty form
                write = "centre added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = pvform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})
        return render(request, 'add.html', {'form': form})
    
    if type == 'team' :    
        if request.method == 'POST':
            form = teamform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = teamform()  # Create a new empty form
                write = "Product added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = teamform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})

    if type == 'fournisseur' :    
        if request.method == 'POST':
            form = fournisseurform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = fournisseurform()  # Create a new empty form
                write = "Product added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = fournisseurform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})

    if type == 'matiere_premiere' :    
        if request.method == 'POST':
            form = matiereform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = matiereform()  # Create a new empty form
                write = "Product added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = matiereform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})        

    if type == 'client' :    
        if request.method == 'POST':
            form = clientform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = clientform()  # Create a new empty form
                write = "Product added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = clientform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})

       
def modify_product(request, id , type):

    if type == 'produit' :
        produits = produit.objects.get(prod_ID=id)
    
        if request.method == 'POST':
            form = productform(request.POST, instance=produits)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = productform(instance=produits)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})

        
    if type == 'client':
        centres = client.objects.get(client_ID=id)
    
        if request.method == 'POST':
            form = clientform(request.POST, instance=client)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = clientform(instance=centres)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})
    
    if type == 'centre':
        centres = centre_pv.objects.get(centre_ID=id)
    
        if request.method == 'POST':
            form = centerform(request.POST, instance=centres)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = centerform(instance=centres)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})
    
    if type == 'fournisseur':
        fournisseurs = fournisseur.objects.get(fournisseur_ID=id)
    
        if request.method == 'POST':
            form = fournisseurform(request.POST, instance=fournisseurs)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = fournisseurform(request.POST ,instance=fournisseurs)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})
    
    if type == 'team':
        teams = team.objects.get(employer_CODE=id)
    
        if request.method == 'POST':
            form = teamform(request.POST, instance=teams)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = teamform(instance=teams)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})

    if type == 'matiere_premiere':
        matiers = matiere_premiere.objects.get(matiere_ID=id)
    
        if request.method == 'POST':
            form = matiereform(request.POST, instance=matiers)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = matiereform(instance=matiers)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})



def delete_product(request,id,type):
    if type == 'produit':
        produits = produit.objects.get(prod_ID=id)
        produits.delete()
        return redirect('list_produit')
    if type =='centre':
        centres = centre_pv.objects.get(centre_ID=id)
        centres.delete()
        return redirect('list_produit')
    if type == 'team':
        teams = team.objects.get(employer_CODE=id)
        teams.delete()
        return redirect('list_produit')
    if type == 'matiere_premiere':
        matiers = matiere_premiere.objects.get(matiere_ID=id)
        matiers.delete()
        return redirect('list_produit')
    if type == 'fournisseur':
        fournisseurs = fournisseur.objects.get(fournisseur_ID=id)
        fournisseurs.delete()
        return redirect('list_produit')
    if type == 'client':
        clients = client.objects.get(client_ID=id)
        clients.delete()
        return redirect('list_produit')



def search_product(request):

    if request.method == 'POST' :
        search = request.POST['passed']
        types = {'searched':search}

        product = produit.objects.filter(prod_NAME__contains=search)
        if product.exists() :
            types.update({'produits' : product })
    
        
        centres = centre_pv.objects.filter(centre_NAME__contains=search)
        if centres.exists() :
            types.update({'centre' : centres})
        
        teams = team.objects.filter(employer_NOM__contains=search)
        if teams.exists() :
            types.update({'team' : teams})
        
        matiers = matiere_premiere.objects.filter(matiere_NAME__contains=search)
        if matiers.exists() :
            types.update({ 'matiere_premiere' : matiers})
        
        clients = client.objects.filter(client_NAME__contains=search)
        if clients.exists() :
            types.update({ 'client' : clients})
        
        fournisseurs = fournisseur.objects.filter(fournisseur_NAME__contains=search)
        if fournisseurs.exists() :
            types.update({'fournisseur' : fournisseurs})
        
        if len(types) > 1 :
            return render(request, 'search.html' , types)
        
        msg = 'no search found :('
        return render(request, 'search.html' , {"searched" : search , "message":msg})



def details(request,id):
    pv = pvs.objects.filter(concerned_center__centre_ID=id)
    return render(request,'details.html',{'pv' : pv , 'id' : id})


def add_vente(request):

    if request.method == 'POST':
        form = venteform(request.POST)

        if form.is_valid():

            prix = form.cleaned_data['prix']
            qte = form.cleaned_data['qte']

            bill = prix * qte

            if_facilite = form.cleaned_data['payement_faciliter']
    
            if if_facilite == True :
                message1 = "facilite mode is available"
            else :
                message1 = "facilite mode isn't available "

            input_value = request.POST.get('combien_regler')
            reste =float(bill) - float(input_value)
            message1 = message1 + f"{reste}"

            
            form.save()  

            

            form = venteform()  
            write = f"Product added and the total is {bill} DA, you can add another . "
            message = write + message1
            return render(request, 'add.html', {'form': form, 'message': message})
    else:
        form = venteform()
        write = "Make sure you have entered all fields."
        return render(request, 'add.html', {'form': form, 'message': write})


def afficher_team(request,id) :
   
    employe = team.objects.filter(centre_pnv__centre_ID = id)

    types={
           "team":employe
          }


    return render(request,"details_employe.html",types)

def select_team(request,id):
    

    employe = team.objects.get(employer_CODE = id)
    id_centre = employe.centre_pnv.centre_ID

    types = {'team' : employe,
             'id':id_centre
            }

    return render(request,"select_team.html",types)    


def pointage(request, id):
    employe = team.objects.get(employer_CODE = id )

    form = PointageForm(request.POST)
    if request.method == 'POST':
       

        if form.is_valid():
            present = form.cleaned_data['employer_Present']
            #absent = form.cleaned_data['employer_Absent']

            if present:
                employe.employer_SALAIRE_JR += 1000
            elif not present:
                employe.employer_SALAIRE_JR -= 500

            employe.save()
            return render(request, 'pointage.html', {'employe': employe, 'form': form})    
    else:
        form = PointageForm()
        return render(request, 'pointage.html', {'employe': employe, 'form': form})


def emprunt(request , id):
    employe = team.objects.get(employer_CODE = id )

    form = empruntform(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            
            total = form.cleaned_data['somme']
            form.save()

            employe.employer_SALAIRE_JR -= total

            employe.save()
            msg = "operation effectuer "
            return render(request, 'emprunt.html', {'employe': employe, 'form': form , 'message':msg})
    else:
        form = empruntform()
        return render(request, 'emprunt.html', {'employe': employe, 'form': form })
    

def profits(request,id,id2):

    centre_sale = vente.objects.filter(produit__prod_ID = id).filter(saled_at__centre_ID = id2)
    
    benefice = []
    for saled in centre_sale:
        benefice_vente = saled.prix - saled.produit.prix_transfert
        benefice.append(benefice_vente)


    length = len(benefice)

    sum = 0 
    for b in benefice :
        sum += b

    if length == 0:
        message = ' no sales '
        profits = 0
    else:
        profits = sum     
        message = f'le taux de benifice pour produit est :'
    return render(request,'profits.html',{'benefice':profits , 'message':message , 'len':length})


def dash_board(request, id):
    ventes = vente.objects.filter(saled_at__centre_ID=id)

    # Calculate total sales for each product
    product_sales = {}
    for ventee in ventes:
        product_name = ventee.produit.prod_NAME
        product_sales[product_name] = product_sales.get(product_name, 0) + ventee.prix

    produits = list(product_sales.keys())
    vente_percentages = list(product_sales.values())

    total_sales = sum(vente_percentages)

    # Calculate sales percentages
    vente_percentages = [prix / total_sales * 100 for prix in vente_percentages]

    plt.figure(figsize=(6, 6))
    plt.pie(vente_percentages, labels=produits, autopct='%1.1f%%')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base1 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render(request, 'dash.html', {'image_base1': image_base1 , 'id':id})


def dash_board2(request, id):
    ventes = vente.objects.filter(saled_at__centre_ID=id)

    # Calculate total sales for each product
    product_sales = {}
    for ventee in ventes:
        product_name = ventee.client_achter.client_NAME
        product_sales[product_name] = product_sales.get(product_name, 0) + ventee.prix

    produits = list(product_sales.keys())
    vente_percentages = list(product_sales.values())

    total_sales = sum(vente_percentages)

    # Calculate sales percentages
    vente_percentages = [prix / total_sales * 100 for prix in vente_percentages]

    plt.figure(figsize=(6, 6))
    plt.pie(vente_percentages, labels=produits, autopct='%1.1f%%')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base2 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render(request, 'dash2.html', {'image_base2': image_base2 , 'id':id})
