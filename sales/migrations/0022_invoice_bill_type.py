# Generated by Django 3.0.7 on 2020-06-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0021_auto_20200621_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='bill_type',
            field=models.CharField(choices=[('Credit', 'Credit'), ('Paid', 'Paid')], max_length=100, null=True),
        ),
    ]
