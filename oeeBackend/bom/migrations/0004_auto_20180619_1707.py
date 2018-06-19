# Generated by Django 2.0.6 on 2018-06-19 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0003_auto_20180619_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bom',
            name='workstation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bom_workstation', to='workstations.Workstation'),
        ),
    ]