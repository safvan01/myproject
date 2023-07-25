# Generated by Django 4.2 on 2023-07-18 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(blank=True, max_length=100, null=True)),
                ('Trainer', models.CharField(blank=True, max_length=100, null=True)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
                ('Closed', models.BooleanField()),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'batches',
            },
        ),
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(blank=True, max_length=100, null=True)),
                ('branchcode', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(choices=[('kerala', 'KERALA'), ('karnataka', 'KARNATAKA'), ('nagaland', 'NAGALAND'), ('tamilnadu', 'TAMILNADU'), ('rajasthan', 'RAJASTHAN'), ('punjab', 'PUNJAB')], max_length=10)),
                ('district', models.CharField(choices=[('kasargod', 'KASARGOD'), ('kannur', 'KANNUR'), ('kozhikkode', 'KOZHKKODE'), ('wayanad', 'WAYANAD'), ('malappuram', 'MLAPPURAM'), ('palakkad', 'PALAKKAD')], max_length=10)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'branches',
            },
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100, null=True)),
                ('address1', models.CharField(max_length=100, null=True)),
                ('address2', models.CharField(max_length=100, null=True)),
                ('address3', models.CharField(max_length=100, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('logo', models.ImageField(null=True, upload_to='')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('kerala', 'KERALA'), ('karnataka', 'KARNATAKA'), ('nagaland', 'NAGALAND'), ('tamilnadu', 'TAMILNADU'), ('rajasthan', 'RAJASTHAN'), ('punjab', 'PUNJAB')], max_length=10)),
                ('districtname', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='enquiry_source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquirysourcename', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'enquiry sources',
                'verbose_name_plural': 'Enquiry sources',
            },
        ),
        migrations.CreateModel(
            name='follow_up_statuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Followupstatusname', models.CharField(blank=True, max_length=100, null=True)),
                ('Followupstatus', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'follow up statuses',
                'verbose_name_plural': 'Follow up statuses',
            },
        ),
        migrations.CreateModel(
            name='master_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Value', models.CharField(blank=True, max_length=100, null=True)),
                ('Type', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'master data',
                'verbose_name_plural': 'Master Data',
            },
        ),
        migrations.CreateModel(
            name='qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qualificationname', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statename', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]