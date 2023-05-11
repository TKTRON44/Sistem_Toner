from django.shortcuts import render, redirect
from .models import Toner
from .forms import SelectTonerForm
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def select_toner(request):
    if request.method == 'POST':
        form = SelectTonerForm(request.POST)
        if form.is_valid():
            toner_id = form.cleaned_data['toner']
            return redirect('confirm_toner', toner_id=toner_id)
    else:
        form = SelectTonerForm()
    return render(request, 'select_toner.html', {'form': form})

def confirm_toner(request, toner_id):
    toner = Toner.objects.get(pk=toner_id)
    toner.quantity -= 1
    toner.save()
    return render(request, 'confirm_toner.html', {'toner': toner})

def toner_list(request):
    toners = Toner.objects.all()
    return render(request, 'toner_list.html', {'toners': toners})

def subtract_toner(request):
    if request.method == 'POST':
        toner_id = request.POST.get('toner_id')
        action = request.POST.get('action')

        toner = Toner.objects.get(id=toner_id)
        if action == 'subtract':
            toner.quantity -= 1
        elif action == 'add':
            toner.quantity += 1

        toner.save()

        return HttpResponse('Ação concluída com sucesso')

def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'retirar':
            pass
        elif action == 'devolver':
            pass
        else:
            toner_id = request.POST.get('toner')
            toner = Toner.objects.get(id=toner_id)
            return redirect('toner_list')  # Redireciona para toner_list.html
    else:
        options = Toner.objects.all()
        return render(request, 'index.html', {'options': options})
