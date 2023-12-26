from django.shortcuts import redirect, render
#from . import models
from .models import centre_pv, fournisseur, produit, client, team, matiere_premiere
from .forms import centerform, clientform, fournisseurform, matiereform, productform, teamform



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


def select(request , id , type) :
   
    types = {}

    if type == 'produit' :
        produits = produit.objects.get(prod_ID = id)
        types = {'produit' : produits}

    if type == 'centre' :
        centres = centre_pv.objects.get(centre_ID = id)
        types = {'centre' : centres}

    if type == 'client' :
        clients = client.objects.get(client_ID = id)
        types = {'client' : clients}

    if type == 'fournisseur' :    
        fournisseurs = fournisseur.objects.get(fournisseur_ID = id)
        types = {'fournisseur' : fournisseurs}


    if type == 'team' :
        employe = team.objects.get(employer_CODE = id)
        types = {'team' : employe}

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
        product = produit.objects.filter(prod_NAME__contains=search)
        if product.exists() :
            return render(request, 'search.html' , {"searched" : search , 'produits' : product})
        else:
            centres = centre_pv.objects.filter(centre_NAME__contains=search)
            if centres.exists() :
                return render(request, 'search.html' , {"searched" : search , 'centre' : centres})
            else:
                teams = team.objects.filter(employer_NOM__contains=search)
                if teams.exists() :
                    return render(request, 'search.html' , {"searched" : search , 'team' : teams})
                else:
                    matiers = matiere_premiere.objects.filter(matiere_NAME__contains=search)
                    if matiers.exists() :
                        return render(request, 'search.html' , {"searched" : search , 'matiere_premiere' : matiers})
                    else:
                        clients = client.objects.filter(client_NAME__contains=search)
                        if clients.exists() :
                            return render(request, 'search.html' , {"searched" : search , 'client' : clients})
                        else:
                            fournisseurs = fournisseur.objects.filter(fournisseur_NAME__contains=search)
                            if fournisseurs.exists() :
                                return render(request, 'search.html' , {"searched" : search , 'fournisseur' : fournisseurs})

