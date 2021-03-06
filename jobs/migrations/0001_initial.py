# Generated by Django 3.2.4 on 2021-06-20 07:50

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MicroTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(help_text='e.g develop website', max_length=300)),
                ('target_date', models.DateTimeField(help_text='e.g 2021-10-25 14:30:59', null=True)),
                ('job_cost', models.PositiveIntegerField(default=0, help_text='currency AED', validators=[django.core.validators.MinValueValidator(0)])),
                ('time_required', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('skills', models.CharField(help_text='e.g coding, data entry', max_length=500, verbose_name='skills')),
                ('people_required', models.PositiveIntegerField(help_text='number of people required e.g 2', validators=[django.core.validators.MinValueValidator(1)])),
                ('job_description', models.CharField(help_text='e.g car website', max_length=1000, verbose_name='job description')),
                ('job_sample', models.FileField(upload_to='job_documents/job_samples/')),
                ('job_instructions', models.FileField(upload_to='job_documents/job_instructions/')),
                ('tc_type', models.CharField(help_text='e.g Senior developer, tester & client', max_length=500, verbose_name='type of tc to be done')),
            ],
        ),
        migrations.CreateModel(
            name='MTOJobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MTORoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MTOJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_to', models.IntegerField(help_text='related to MTO')),
                ('due_date', models.DateField()),
                ('assigned_date', models.DateField()),
                ('fees', models.FloatField()),
                ('rating_evaluation', models.IntegerField()),
                ('payment_status', models.IntegerField()),
                ('completed_date', models.DateField()),
                ('output_path', models.FileField(upload_to='')),
                ('evaluation_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.evaluationstatus')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jobs.microtask')),
            ],
        ),
        migrations.CreateModel(
            name='MTOAdminUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('varal_role_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jobs.mtoroles')),
            ],
            options={
                'verbose_name_plural': 'MTO Admin Users',
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='microtask',
            name='cat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.mtojobcategory'),
        ),
        migrations.CreateModel(
            name='MALRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(help_text='Mal identification', max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('assembly_line_id', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('assembly_line_name', models.TextField()),
                ('person_name', models.TextField(help_text='Name of the person in charge')),
                ('output', models.FilePathField(help_text='Link of the output folder', path='job_documents/output')),
                ('target_date', models.DateField()),
                ('total_budget', models.IntegerField(help_text='Total budget allocated for the job')),
                ('job_description', models.TextField()),
                ('job_sample', models.FileField(upload_to='job sample')),
                ('job_instructions', models.FileField(upload_to='jobs instruction')),
                ('job_quantity', models.IntegerField()),
                ('input_folder', models.FilePathField(help_text='Link of the Input folder', path='job_documents/input')),
                ('micro_task', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='jobs.microtask')),
            ],
        ),
        migrations.AddField(
            model_name='evaluationstatus',
            name='description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.microtask'),
        ),
    ]
