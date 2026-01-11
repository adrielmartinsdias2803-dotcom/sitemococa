from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from condicaoRiscoMococaProjeto.models import FuncionarioProfile



@login_required(login_url='/login/')
def dashboard(request):
    instanceFuncionario = FuncionarioProfile.objects.get(user=request.user) if request.user.is_authenticated else None 
    cargoUser = instanceFuncionario.cargo.nome
    
    return render(request, 'dashboard.html', {
        'cargoUser': cargoUser})