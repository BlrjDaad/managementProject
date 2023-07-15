# Generated by Django 4.2.2 on 2023-07-05 13:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_department_company'),
        ('invitations', '0004_alter_baseinvitation_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinvitation',
            name='token',
            field=models.TextField(default=uuid.UUID('8d1ff460-7dab-405e-abe7-8c485f7d25a6')),
        ),
        migrations.CreateModel(
            name='EmployeeInvitation',
            fields=[
                ('baseinvitation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invitations.baseinvitation')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='company.department')),
            ],
            bases=('invitations.baseinvitation',),
        ),
    ]
