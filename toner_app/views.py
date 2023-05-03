from django.shortcuts import render, redirect
from .models import Toner
from .forms import SelectTonerForm
from django.http import JsonResponse
from django.shortcuts import render
from toner_app.models import Toner


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
    data = [{'model': toner.model, 'quantity': toner.quantity} for toner in toners]
    return JsonResponse(data, safe=False)

def retirada_devolucao(request):
    toners = Toner.objects.all()

    context = {'toners': toners}

    return render(request, 'retirada_devolucao.html', context)