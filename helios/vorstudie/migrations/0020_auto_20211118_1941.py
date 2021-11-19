# Generated by Django 3.1.13 on 2021-11-18 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0020_auto_20211118_1902'),
        ('vorstudie', '0019_auto_20211118_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investitionskosten',
            name='flaeche',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investitionskosten',
            name='gewerk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gewerk'),
        ),
        migrations.AlterField(
            model_name='investitionskosten',
            name='investitionskosten_Kw_Gewerk_Erzeugung',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investitionskosten',
            name='investitionskosten_Kw_Gewerk_Erzeugung2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investitionskosten',
            name='investitionskosten_m2_gewerk',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investitionskosten',
            name='leistung',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vorstudie.leistung'),
        ),
        migrations.AlterField(
            model_name='investitionskosten',
            name='stammdateb_kosten_elektro',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investitionskosten',
            name='stammdaten_kosten_hlks_abgabe',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investitionskosten',
            name='stammdaten_kosten_hlks_erzeugung',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investitionskosten',
            name='umwandlung',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.umwandlung'),
        ),
    ]
