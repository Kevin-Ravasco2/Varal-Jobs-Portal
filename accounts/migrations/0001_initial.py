# Generated by Django 3.2.4 on 2021-06-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MTOPaymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField(help_text='related to micro task')),
                ('assigned_to', models.IntegerField(help_text='related to MTO')),
                ('payment_id', models.IntegerField()),
                ('payment_date', models.DateField()),
                ('fees', models.FloatField()),
            ],
        ),
    ]
