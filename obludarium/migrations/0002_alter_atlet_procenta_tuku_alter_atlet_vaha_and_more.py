# Generated by Django 4.2 on 2023-04-12 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obludarium', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atlet',
            name='procenta_tuku',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='atlet',
            name='vaha',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='atlet',
            name='vyska',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vykon',
            name='cmj',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vykon',
            name='push_ups',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vykon',
            name='squat',
            field=models.IntegerField(null=True),
        ),
    ]
