# Generated by Django 4.2 on 2023-04-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pizza/'),
        ),
    ]