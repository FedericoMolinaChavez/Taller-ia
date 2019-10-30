# Generated by Django 2.2.6 on 2019-10-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Jury', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=50)),
                ('jury', models.ManyToManyField(to='Jury.Jury')),
            ],
        ),
    ]