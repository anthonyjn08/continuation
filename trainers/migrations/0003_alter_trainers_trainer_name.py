# Generated by Django 3.2 on 2022-10-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_alter_trainers_trainer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainers',
            name='trainer_name',
            field=models.CharField(max_length=100),
        ),
    ]
