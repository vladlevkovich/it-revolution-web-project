# Generated by Django 4.2 on 2023-04-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_pizza'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ingredient',
            field=models.ManyToManyField(blank=True, null=True, to='order.ingredient'),
        ),
    ]
