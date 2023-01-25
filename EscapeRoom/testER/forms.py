from django import forms
from .models import Pokoj, EscapeRoom,Promocje,Rezerwacje
#from django.utils.timezone import datetime
from datetime import datetime

class AddRoomForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(AddRoomForm, self).__init__(*args, **kwargs)
        self.fields['firma'].queryset = EscapeRoom.objects.filter(wlasc_id=user.profile)

    class Meta:
        model = Pokoj
        fields = ['nazwa', 'kategoria', 'opis', 'trudnosc', 'max_czas', 'kat_cenowa','firma','promocje']


class AddResForm(forms.ModelForm):
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    godzina = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    # def clean(self):
    #     cleaned_data = super(AddResForm,self).clean()
    #     if self.data > datetime.now().date():
    #         raise forms.ValidationError("Nie można wybrać tej daty! :(")
    #     return cleaned_data

    class Meta:
        model = Rezerwacje
        template_name = 'testER/add_reservation.html'
        fields = ['data', 'godzina']

class AddPromForm(forms.ModelForm):
    data_rozpoczecia = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    data_zakonczenia = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Promocje
        template_name = 'testER/add_promotion.html'
        fields = ['nazwa', 'data_rozpoczecia', 'data_zakonczenia', 'procent']