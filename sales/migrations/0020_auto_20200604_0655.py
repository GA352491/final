# Generated by Django 3.0.6 on 2020-06-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0019_auto_20200603_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]