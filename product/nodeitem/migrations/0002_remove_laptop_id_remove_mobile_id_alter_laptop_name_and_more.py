# Generated by Django 4.0.3 on 2022-03-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodeitem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='id',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='id',
        ),
        migrations.AlterField(
            model_name='laptop',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
