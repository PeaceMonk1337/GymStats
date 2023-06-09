# Generated by Django 4.2 on 2023-04-12 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=50)),
                ('prijmeni', models.CharField(max_length=50)),
                ('vyska', models.IntegerField(max_length=3)),
                ('vaha', models.IntegerField(max_length=3)),
                ('sex', models.CharField(max_length=1)),
                ('procenta_tuku', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Vykon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('push_ups', models.IntegerField(max_length=3)),
                ('cmj', models.IntegerField(max_length=2)),
                ('row_500', models.CharField(max_length=20)),
                ('squat', models.IntegerField(max_length=10)),
                ('atlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obludarium.atlet')),
            ],
        ),
    ]
