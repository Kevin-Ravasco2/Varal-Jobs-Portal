# Generated by Django 3.2.4 on 2021-06-13 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTO',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('paypal_id', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user',),
        ),
    ]
