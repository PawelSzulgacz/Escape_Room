from django import forms
from .models import Pokoj, EscapeRoom,Promocje

class AddRoomForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(AddRoomForm, self).__init__(*args, **kwargs)
        self.fields['firma'].queryset = EscapeRoom.objects.filter(wlasc_id=user.profile)

    class Meta:
        model = Pokoj
        fields = ['nazwa', 'kategoria', 'opis', 'trudnosc', 'max_czas', 'kat_cenowa','firma','promocje']

"""
class AddPromotionForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(AddPromotionForm, self).__init__(*args, **kwargs)
        self.fields['pokoje'].queryset = EscapeRoom.objects.filter(wlasc_id=user.profile)

    class Meta:
        model = Promocje
        fields = ['nazwa','procent','data_rozpoczecia','data_zakonczenia',]
"""