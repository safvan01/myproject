# Generated by Django 4.2.2 on 2023-07-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Alternative_Email',
            field=models.EmailField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Alternative_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='City',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Street',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
