# Generated by Django 4.2.2 on 2023-06-27 15:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinvitation',
            name='token',
            field=models.TextField(default=uuid.UUID('4faaa068-087c-40ca-b4a3-694a011058a3')),
        ),
    ]
