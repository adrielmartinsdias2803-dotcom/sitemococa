
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('condicaoRiscoMococaProjeto:dashboard')
        return super().dispatch(request, *args, **kwargs)