# Generated by Django 4.1.1 on 2022-09-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('varauskalenteri', '0005_tapahtuma_nakyvissa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tapahtuma',
            name='nakyvissa',
            field=models.BooleanField(default=False, verbose_name='Visible'),
        ),
    ]
