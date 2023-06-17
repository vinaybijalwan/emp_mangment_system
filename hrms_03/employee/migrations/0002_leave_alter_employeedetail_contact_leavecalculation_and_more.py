# Generated by Django 4.1.5 on 2023-06-08 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('CL', 'Casual Leave'), ('EL', 'Earned Leave'), ('LWP', 'Leave Without Pay'), ('SL', 'Sick Leave')], max_length=3)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('approved', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='LeaveCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_approval', models.BooleanField(default=False)),
                ('total_days', models.PositiveIntegerField()),
                ('leave', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.leave')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hod_approval', models.BooleanField(default=False)),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.leave')),
            ],
        ),
    ]
