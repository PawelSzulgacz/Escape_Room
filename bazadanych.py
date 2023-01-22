from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Uzytkownik(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.IntegerField()

class Wlasciciel(models.Model):
    user_id = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)
    login = models.CharField(max_length=30)
    haslo = models.CharField(max_length=30)

class Klient(models.Model):
    user_id = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)
    login = models.CharField(max_length=30)
    haslo = models.CharField(max_length=30)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=40)

class Pokoj(models.Model):
    nazwa = models.CharField(max_length=40)
    kategoria = models.CharField(max_length=40)
    trudnosc = models.IntegerField()
    max_czas = models.IntegerField()
    kat_cenowa = models.ForeignKey(Uzytkownik, on_delete=models.NULL)
    promocje = models.ForeignKey(null=True)

class Odwiedziny(models.Model):
    ukonczony = models.BooleanField()
    czas_wyjscia = models.IntegerField()
    klient_id = models.ForeignKey(Pokoj, on_delete=models.SET_NULL)
    pokoj_id = models.ForeignKey(Klient, on_delete=models.SET_NULL)
    data = models.DateField()

class EscapeRoom(models.Model):
    nazwa = models.CharField(max_length=50)
    adres = models.CharField(max_length=50)
    telefon = models.CharField(max_length=11)
    opis = models.CharField(max_length=500)
    wlasc_id = models.ForeignKey(Wlasciciel, on_delete=models.CASCADE)

class Recenzje(models.Model):
    klient_id = models.ForeignKey(Klient, on_delete=models.SET_NULL)
    pokoj_id = models.ForeignKey(Pokoj, on_delete=models.SET_NULL)
    rec_id = models.AutoField()
    ocena = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    komentarz = models.CharField(max_length=500, blank=True)


class Ceny(models.Model):
    kat_cenowa = models.IntegerField(primary_key=True)
    cena = models.DecimalField(primary_key=True, max_digits=5, decimal_places=2)

class Promocje(models.Model):
    data_rozpoczecia = models.DateField()
    data_zakonczenia = models.DateField()

class Rezerwacje(models.Model):
    data = models.DateField()
    godzina = models.TimeField()
    klient_id = models.ForeignKey(Klient, on_delete=models.CASCADE)
    pokoj_id = models.ForeignKey(Pokoj, on_delete=models.CASCADE)


