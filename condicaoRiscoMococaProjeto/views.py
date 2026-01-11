from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from condicaoRiscoMococaProjeto.models import FuncionarioProfile



@login_required(login_url='/login/')
def dashboard(request):
    if request.user.is_superuser:
        cargoUser = "Administrador"
    else:
        instanceFuncionario = FuncionarioProfile.objects.get(user=request.user)
        cargoUser = instanceFuncionario.cargo.nome

    return render(request, 'dashboard.html', {
        'cargoUser': cargoUser
    }) 