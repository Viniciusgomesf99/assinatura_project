from django.shortcuts import render, redirect
from .forms import AssinaturaForm

def captura_assinatura(request):
    if request.method == 'POST':
        form = AssinaturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = AssinaturaForm()
    return render(request, 'assinatura_app/captura_assinatura.html', {'form': form})

def sucesso(request):
    return render(request, 'assinatura_app/sucesso.html')