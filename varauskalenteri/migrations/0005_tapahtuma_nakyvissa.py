# Generated by Django 4.1.1 on 2022-09-26 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('varauskalenteri', '0004_alter_tapahtuma_kuvaus_alter_tapahtuma_loppu'),
    ]

    operations = [
        migrations.AddField(
            model_name='tapahtuma',
            name='nakyvissa',
            field=models.BooleanField(default=False),
        ),
    ]
