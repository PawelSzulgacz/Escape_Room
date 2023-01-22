# Generated by Django 4.1.5 on 2023-01-22 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_user_type'),
        ('testER', '0003_pokoj_firma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wlasciciel',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='escaperoom',
            name='wlasc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='odwiedziny',
            name='pokoj_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='recenzje',
            name='klient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='rezerwacje',
            name='klient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.DeleteModel(
            name='Klient',
        ),
        migrations.DeleteModel(
            name='Uzytkownik',
        ),
        migrations.DeleteModel(
            name='Wlasciciel',
        ),
    ]
