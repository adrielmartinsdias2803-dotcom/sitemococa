from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import FuncionarioProfile, Cargo

# 1. Registra o model de Cargos para você poder criar novos cargos pelo painel
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

# 2. Mantemos o Inline do Perfil dentro do User
class FuncionarioProfileInline(admin.StackedInline):
    model = FuncionarioProfile
    can_delete = False
    verbose_name_plural = 'Informações do Funcionário'
    fk_name = 'user'
    # Como agora é ForeignKey, o Django já cria um dropdown automático buscando do banco

class UserAdmin(BaseUserAdmin):
    inlines = (FuncionarioProfileInline,)
    
    list_display = ('username', 'first_name', 'get_cargo', 'is_staff')

    def get_cargo(self, instance):
        if hasattr(instance, 'profile') and instance.profile.cargo:
            return instance.profile.cargo.nome
        return '-'
    get_cargo.short_description = 'Cargo'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)