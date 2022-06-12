from datetime import date, datetime
from time import timezone
from django.db import models
from django.shortcuts import render
from django.shortcuts import redirect
from participants.forms import participantID, participants
from participants.models import Competitor
# Create your views here.

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
def ageDivision(_age):
    if(_age >= 5 & _age < 12):
        return " niño"
    elif(_age >=12 & _age < 18):
        return "juvenil"
    elif(_age >=18 & _age < 35 ):
        return "adulto"
    elif(_age >= 35):
        return "master"
    else:
        return "adulto"

def register(request):
    if('verify' in request.GET):
        print("hola mundo!")
    if request.method == 'POST':
        form = participants(data= request.POST,files=request.FILES)
        print(form.errors)
        if (form.is_valid()):
            bday=   form.cleaned_data['fechaNacimiento'].replace("-","/") + ' 00:00:00'
            edad= age(datetime.strptime(bday, '%Y/%m/%d %H:%M:%S'))

            competitor = Competitor()
            competitor.nombres = form.cleaned_data['nombres']
            competitor.apellidos= form.cleaned_data['apellidos']
            competitor.documento= form.cleaned_data['documento']
            competitor.genero= form.cleaned_data['genero']
            competitor.academia= form.cleaned_data['academia']
            competitor.cinturon= form.cleaned_data['cinturon']
            competitor.pais= form.cleaned_data['pais']
            competitor.ciudad= form.cleaned_data['ciudad']
            competitor.edad= edad
            competitor.fechaNacimiento = bday
            competitor.categoriaEdad= ageDivision(edad)
            competitor.categoriaPeso=form.cleaned_data['Categoria']
            competitor.comprobantePago = form.cleaned_data['filename']
            competitor.verificado = False
            competitor.save()
            return redirect (pendigVerification)
    print(request.GET)
    return render(request, 'participants/registrationForm.html', {'form' : participants} )

def pendigVerification(request):
    return render(request, 'participants/pending.html')

def verified(request):
    return render(request, 'participants/success.html')

def participantNotFound(request):
    return render(request, 'participants/notFound.html')

def hasPendingVerification(request):
    if request.method == "POST":
        docForm = participantID(data= request.POST)
        if(docForm.is_valid()):
            print(docForm.cleaned_data['documento'])
            
            try: 
                competitor= Competitor.objects.get(documento = docForm.cleaned_data['documento'])
                return redirect('verified') if competitor.verificado else redirect(pendigVerification)
            except :
                return redirect(participantNotFound)
    return render(request, 'participants/verify.html',{'form': participantID})

def weight(request):
    return render(request, 'participants/tablaPesos.html')

def pay(request):
    return render(request, 'participants/pago.html')
