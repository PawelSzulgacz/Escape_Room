from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Profile
from django.urls import reverse
from django.shortcuts import render

class Promocje(models.Model):
    data_rozpoczecia = models.DateField()
    data_zakonczenia = models.DateField()
    procent = models.DecimalField(max_digits=5, decimal_places=2,null=True,)

class Ceny(models.Model):
    kat_cenowa = models.IntegerField(primary_key=True)
    cena = models.DecimalField(max_digits=5, decimal_places=2)

class EscapeRoom(models.Model):
    nazwa = models.CharField(max_length=50)
    adres = models.CharField(max_length=50)
    telefon = models.CharField(max_length=11)
    wlasc_id = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='company')

class Pokoj(models.Model):
    nazwa = models.CharField(max_length=40)
    kategoria = models.CharField(max_length=40)
    trudnosc = models.IntegerField()
    max_czas = models.IntegerField()
    opis = models.CharField(max_length=500,default="brak")
    firma = models.ForeignKey(EscapeRoom, default=1, on_delete=models.CASCADE)
    kat_cenowa = models.ForeignKey(Ceny, default=1,on_delete=models.SET_DEFAULT)
    promocje = models.ForeignKey(Promocje,blank = True,null=True,on_delete = models.SET_NULL)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


class Odwiedziny(models.Model):
    ukonczony = models.BooleanField()
    czas_wyjscia = models.IntegerField()
    klient_id = models.ForeignKey(Profile, null=True,on_delete=models.SET_NULL)
    pokoj_id = models.ForeignKey(Pokoj,  null=True,on_delete=models.SET_NULL)
    data = models.DateField()



class Recenzje(models.Model):
    rec_id = models.AutoField(primary_key = True)
    klient_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pokoj_id = models.ForeignKey(Pokoj, on_delete=models.CASCADE)
    ocena = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    komentarz = models.CharField(max_length=500, blank=True)
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pokoj_id.id})

class Rezerwacje(models.Model):
    data = models.DateField()
    godzina = models.TimeField()
    klient_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pokoj_id = models.ForeignKey(Pokoj, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pokoj_id.id})


