# Generated by Django 4.2.2 on 2023-09-26 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0003_alter_baseinvitation_token'),
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='invitation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='invitations.baseinvitation'),
        ),
    ]