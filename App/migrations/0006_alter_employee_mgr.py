# Generated by Django 4.1.7 on 2023-04-08 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_employee_hiredate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='MGR',
            field=models.IntegerField(null=True),
        ),
    ]
