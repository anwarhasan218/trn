# Generated by Django 5.2.4 on 2025-07-18 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='اسم المعلم')),
                ('national_id', models.CharField(max_length=20, unique=True, verbose_name='الرقم القومي')),
                ('record_number', models.CharField(max_length=20, unique=True, verbose_name='رقم السجل')),
                ('subject', models.CharField(max_length=100, verbose_name='المادة')),
                ('stage', models.CharField(max_length=50, verbose_name='المرحلة التعليمية')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='اسم البرنامج التدريبي')),
                ('target_group', models.CharField(max_length=100, verbose_name='الفئة المستهدفة')),
                ('stage', models.CharField(max_length=50, verbose_name='المرحلة التعليمية')),
                ('start_date', models.DateField(verbose_name='تاريخ بداية التدريب')),
                ('end_date', models.DateField(verbose_name='تاريخ نهاية التدريب')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bahira_training.teacher', verbose_name='المعلم')),
                ('training_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bahira_training.trainingprogram', verbose_name='البرنامج التدريبي')),
            ],
            options={
                'verbose_name': 'انتساب معلم لتدريب',
                'verbose_name_plural': 'انتسابات المعلمين للتدريبات',
                'unique_together': {('teacher', 'training_program')},
            },
        ),
    ]
