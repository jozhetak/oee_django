# Generated by Django 2.0.6 on 2018-06-20 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_orders_data', '0002_auto_20180620_1652'),
        ('stops', '0004_auto_20180610_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobStop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(blank=True, null=True)),
                ('close_datetime', models.DateTimeField(blank=True, null=True)),
                ('stop_time', models.FloatField(blank=True, null=True)),
                ('stop_description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('job_order_data_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='jobstop_q_issue', to='job_orders_data.JobOrderData')),
                ('stop_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='jobstop_q_issue', to='stops.Stop')),
            ],
        ),
    ]