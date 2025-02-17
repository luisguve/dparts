# Generated by Django 5.1.3 on 2025-01-11 00:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_amount_vef'),
        ('payment_config', '0005_alter_dollarexchangehistory_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='method_of_payment',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='payment_config.paymentmethod', verbose_name='Metodo de pago'),
        ),
    ]
