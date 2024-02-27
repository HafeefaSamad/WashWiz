# Generated by Django 5.0.2 on 2024-02-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='timeslot',
            field=models.IntegerField(blank=True, choices=[(1, '9-10'), (2, '10-11'), (3, '11-12'), (4, '12-1'), (5, '2-3'), (6, '3-4'), (7, '4-5')], null=True),
        ),
    ]
