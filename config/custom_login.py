from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy 

class CustomLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('condicaoRiscoMococaProjeto:dashboard')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('condicaoRiscoMococaProjeto:dashboard')
        return super().dispatch(request, *args, **kwargs)