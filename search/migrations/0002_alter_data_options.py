# Generated by Django 4.0.6 on 2022-08-03 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ('ent_seq', 'keb', 'reb', 'trans_det')},
        ),
    ]
