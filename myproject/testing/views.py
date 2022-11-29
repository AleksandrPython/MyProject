from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bdquestions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'pagehome.html')

def pagetesting(request):
    questions = Bdquestions.objects.all()
    return render(request, 'pagetesting.html', {'questions': questions})

def newquestion(request):
    nfio = request.POST.get('newfio')
    nquestion = request.POST.get('newq')
    nanswer1 = request.POST.get('newa1')
    nanswer2 = request.POST.get('newa2')
    ntrueanswer = request.POST.get('newtrue')
    quest = Bdquestions()
    quest.fio = nfio
    quest.questions = nquestion
    quest.answer1 = nanswer1
    quest.answer2 = nanswer2
    quest.trueanswer = ntrueanswer
    quest.save()
    return HttpResponseRedirect('pagetesting')

def pagequestion(request, id):
    pagequestion = Bdquestions.objects.get(id=id)
    return render(request, 'pagequest.html', {'question': pagequestion}) 

def pageeditquest(request, id):
    pagequestion = Bdquestions.objects.get(id=id)
    return render(request, 'pageeditq.html', {'question': pagequestion}) 

def pagetest(request):
    quest = Bdquestions.objects.get(id=1)
    return render(request, 'pagetest.html', {'question': quest}) 

def checkboxes(request):
    quest = Bdquestions.objects.get(id=1)
    if request.method == 'POST':
        otvet = request.POST.getlist('answer')
        num1 = int(otvet[0])
        num2 = int(quest.trueanswer)
        
        if num1==1 and num2==1: 
            print(num1)
            print(num2)        
            return render(request, 'pagerezgr.html', {'question': quest})
        if num1!=1 and num2==1:
            print(num2)
            return render(request, 'pagerezgr.html', {'question': quest})
        else:
            return render(request, 'pagerezgr.html', {'question': quest})

def saveeditquest(request, id):
    pagequestion = Bdquestions.objects.get(id=id)
    nfio = request.POST.get('newfio')
    nquestion = request.POST.get('newq')
    nanswer1 = request.POST.get('newa1')
    nanswer2 = request.POST.get('newa2')
    ntrueanswer = request.POST.get('newtrue')
    pagequestion.fio = nfio
    pagequestion.questions = nquestion
    pagequestion.answer1 = nanswer1
    pagequestion.answer2 = nanswer2
    pagequestion.trueanswer = ntrueanswer
    pagequestion.save()
    return HttpResponseRedirect('/pagetesting')

def pagedeletquest(request, id):
    pagequestion = Bdquestions.objects.get(id=id)
    pagequestion.delete()
    return HttpResponseRedirect('/pagetesting')

def pagereg(request):
    if request.method == 'POST':
        nlog = request.POST.get('login')
        nmail = request.POST.get('email')
        npass = request.POST.get('password')
        user = User.objects.create_user(nlog, nmail, npass)
        user.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'pagereg.html')

def pagein(request):
    if request.method == 'POST':
        log = request.POST.get('login')
        passin = request.POST.get('password')
        user = authenticate(username=log, password=passin)
        if user is not None:
            print('Успешная авторизация')
            return HttpResponseRedirect('/profile')
        else:
            print('Отказано в доступе')
            return HttpResponseRedirect('/pagein')
    else:
        return render(request, 'pagein.html')

