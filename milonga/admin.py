from django.contrib import admin
from milonga.models import Pessoa, Danca,  Milonga
from milonga.forms import ParDancaForm


class MilongaAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora_inicio', 'hora_fim')


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo')


class DancaAdmin(admin.ModelAdmin):
    list_display = ('cavalheiro', 'dama', 'hora_inicio', 'hora_fim', 'milonga')
    form = ParDancaForm


admin.site.register(Milonga, MilongaAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Danca, DancaAdmin)