# Generated by Django 3.1.7 on 2021-04-05 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0005_auto_20210404_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendas',
            name='email_cliente',
        ),
    ]