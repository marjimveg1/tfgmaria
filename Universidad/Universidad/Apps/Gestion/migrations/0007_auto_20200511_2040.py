# Generated by Django 3.0.4 on 2020-05-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0006_auto_20200511_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='quiereNot',
            field=models.BooleanField(default=False),
        ),
    ]
