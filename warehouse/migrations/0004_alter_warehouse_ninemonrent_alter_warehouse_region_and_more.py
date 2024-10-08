# Generated by Django 4.2 on 2024-09-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_alter_warehouse_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='ninemonrent',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='region',
            field=models.CharField(choices=[('Hong_Kong_Island', 'Hong Kong Island'), ('New_Territories', 'New Territories'), ('Kowloon', 'Kowloon')], max_length=50),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='sixmonrent',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='threemonrent',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
