# Generated by Django 4.2.6 on 2023-10-18 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_room_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('closed', 'Closed'), ('waiting', 'Waiting')], default='waiting', max_length=20),
        ),
    ]
