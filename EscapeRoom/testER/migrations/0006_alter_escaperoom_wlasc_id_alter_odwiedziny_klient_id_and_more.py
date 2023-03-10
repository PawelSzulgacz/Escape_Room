# Generated by Django 4.1.5 on 2023-01-22 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_user_type'),
        ('testER', '0005_remove_escaperoom_opis_pokoj_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escaperoom',
            name='wlasc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='odwiedziny',
            name='klient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='odwiedziny',
            name='pokoj_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testER.pokoj'),
        ),
    ]
