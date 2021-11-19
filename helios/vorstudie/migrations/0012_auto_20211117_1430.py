# Generated by Django 3.1.13 on 2021-11-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vorstudie', '0011_remove_technikflaechen_name_technik'),
    ]

    operations = [
        migrations.AddField(
            model_name='technikflaechen',
            name='leistung_pro_m2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='technikflaechen',
            name='luftmenge',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='technikflaechen',
            name='zentralengroessen',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='technikflaechen',
            name='zentralentyp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
