from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Profile
from django.urls import reverse
from django.shortcuts import render

class Promocje(models.Model):
    nazwa = models.CharField(max_length=50,default='promocja')
    data_rozpoczecia = models.DateField(null=True)
    data_zakonczenia = models.DateField(null=True)
    procent = models.IntegerField(null=True,validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])

    def __str__(self):
        return f'{self.nazwa} - {self.procent}% od {self.data_rozpoczecia} do {self.data_zakonczenia}'

    def get_absolute_url(self):
        return reverse('Escape_Room_app')

class Ceny(models.Model):
    kat_cenowa = models.IntegerField(primary_key=True)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.cena)
class EscapeRoom(models.Model):
    nazwa = models.CharField(max_length=50)
    adres = models.CharField(max_length=50)
    telefon = models.CharField(max_length=11)
    wlasc_id = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='company')

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('Escape_Room_app')

class Pokoj(models.Model):
    nazwa = models.CharField(max_length=40)
    type = [('P', 'Przygodowy'),
            ('T', 'Thriller'),
            ('H', 'Horror'),
            ('Hi', 'Historyczny'),
            ('F', 'Fabularny'),
            ('A', 'Akcja'),
            ('Fan', 'Fantasy'),
            ('K', 'Kryminalny'),
            ]
    typet = [
        ('Ł', 'Łatwy'),
        ('Ś', 'Średni'),
        ('T', 'Trudny'),
    ]
    kategoria = models.CharField(max_length=40,choices=type)
    trudnosc = models.CharField(choices=typet,max_length=10)
    max_czas = models.IntegerField(validators=[
            MaxValueValidator(180),
            MinValueValidator(60)
        ])
    opis = models.CharField(max_length=500,default="brak")
    firma = models.ForeignKey(EscapeRoom, default=1, on_delete=models.CASCADE)
    kat_cenowa = models.ForeignKey(Ceny, default=1,on_delete=models.SET_DEFAULT)
    promocje = models.ForeignKey(Promocje,blank=True,null=True,on_delete = models.SET_NULL)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


class Odwiedziny(models.Model):
    ukonczony = models.BooleanField()
    czas_wyjscia = models.IntegerField(validators=[
            MinValueValidator(60)
        ])
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


