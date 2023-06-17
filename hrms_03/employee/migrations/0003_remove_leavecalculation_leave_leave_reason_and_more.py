# Generated by Django 4.1.5 on 2023-06-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_leave_alter_employeedetail_contact_leavecalculation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavecalculation',
            name='leave',
        ),
        migrations.AddField(
            model_name='leave',
            name='reason',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='LeaveApplication',
        ),
        migrations.DeleteModel(
            name='LeaveCalculation',
        ),
    ]
