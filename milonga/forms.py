from django.forms import ModelForm
from milonga.models import Danca


class ParDancaForm(ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cavalheiro = cleaned_data['cavalheiro']
        dama = cleaned_data['dama']
        hora = cleaned_data['hora_inicio']

        dancas_cavalheiro = Danca.objects.filter(cavalheiro=cavalheiro, hora_inicio__lte=hora, hora_fim__gt=hora)

        if dancas_cavalheiro.exists():
             self.add_error('cavalheiro', "O cavalheiro já está dançando")

        dancas_dama = Danca.objects.filter(dama=dama, hora_inicio__lte=hora, hora_fim__gt=hora)

        if dancas_dama.exists():
             self.add_error('dama', "A dama já está dançando")

    class Meta:
        model = Danca
        fields = ['cavalheiro', 'dama', 'milonga', 'hora_inicio', 'hora_fim']