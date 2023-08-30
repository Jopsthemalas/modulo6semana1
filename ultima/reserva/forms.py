from django import forms
from reserva.models import Reserva
from datetime import date

class Reservaform (forms.ModelForm):

    

    def clean_data (self):
        turno = self.data ['turno']
        data = self.cleaned_data ['data']
        hoje =  date.today()
        if data < hoje :
            raise forms.ValidationError ('não é posivel realizar uma reserva para o passado!')
        
        x = Reserva.objects.filter(turno=turno, data=data).count()

        if x > 4 :
            raise forms.ValidationError ('so é posivel fazer 4 reserva no dia!')

        return data

    

    class Meta :

        model = Reserva
        fields = [
            'nome','email','nome_pet','data','turno','tamanho','observacoes'
        ]