from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from .models import offres
from django.contrib.auth.models import User, auth
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import offresForm
import psycopg2
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def update(request,pk):

    offre = offres.objects.get(id=pk)
    form = offresForm(instance=offre)

    if request.method == 'POST':
        form = offresForm(request.POST,instance=offre)
        if form.is_valid() :
            form.save()
            return redirect("publish")
            
    context={'form':form}
    return render(request, 'offre_form.html', context)

def supprimer(request, pk): 
    offre = offres.objects.get(id=pk) 
    if request.method =="POST":  
        offre.delete()  
        return redirect("publish") 
   
    context ={'item':offre}    
    return render(request, "delete.html", context) 

def afficher(request):
    offre = offres.objects.all()
    return render(request,'publish.html', {'offre': offre})



def publication(request):
    return render(request, 'publish.html')


def submitoffer(request):
    
    if request.method == 'POST':
            if request.POST.get('Poste') and request.POST.get('Profil') and request.POST.get('Compétences téchniques') and request.POST.get('Qualités personelles requises') and request.POST.get('Type de contrat') and request.POST.get('Lieu') and request.POST.get('Durée') and request.POST.get('Date de démarrage') and request.POST.get('Expérience minimale') :
                offre = offres()
                offre.Poste= request.POST.get('Poste')
                offre.Profil= request.POST.get('Profil')
                offre.Compétences= request.POST.get('Compétences téchniques')
                offre.Qualités= request.POST.get('Qualités personelles requises')
                offre.Contrat= request.POST.get('Type de contrat')
                offre.Lieu= request.POST.get('Lieu')
                offre.Durée= request.POST.get('Durée')
                offre.Démarrage= request.POST.get('Date de démarrage')
                offre.Expérience= request.POST.get('Expérience minimale')
                offre.save()
                return redirect("publish")  

    else:
                return render(request,'hello.html')

from django.contrib.auth.hashers import make_password
def signin(request):
    
    
    if request.method=='POST':
        email = request.POST.get('email')
        conn = psycopg2.connect(user = "postgres", password= 'Hafsaadem1', database = 'site', host = "localhost")
        curs = conn.cursor()
        curs.execute("select username from auth_user where email ='{}'".format(email))
        data = curs.fetchall()
        curs.close()
        conn.close()
        password = request.POST.get('password')
        user = None
        if len(data) > 0: user = auth.authenticate(username=data[0][0], email=email,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("offres")
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')
    else:
        return render(request,"index.html")

def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 
        if password2==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1,email=email)
                user.save()
                messages.info(request,'user created')
        else:
            messages.info(request,'passwords not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')