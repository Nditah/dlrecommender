# Generated by Django 2.1.3 on 2018-11-09 13:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Statistics', 'Statistics'), ('Electronic Engineering', 'Electronic Engineering'), ('Library Science', 'Library Science')], max_length=50)),
                ('subcategory', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Statistics', 'Statistics'), ('Electronic Engineering', 'Electronic Engineering'), ('Library Science', 'Library Science')], max_length=50)),
                ('keywords', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rated', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitallibrary.Item')),
            ],
            options={
                'ordering': ('rated',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('age', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(15)])),
                ('department', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Statistics', 'Statistics'), ('Electronic Engineering', 'Electronic Engineering'), ('Library Science', 'Library Science')], max_length=200)),
                ('specialization', models.CharField(choices=[('Software Development', 'Software Development'), ('System Design', 'System Design'), ('System Analysis', 'System Analysis'), ('Programming Languages', 'Programming Languages'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Bayesian Inference', 'Bayesian Inference'), ('Nonlinear programming', 'Nonlinear programming'), ('Stochastic Programming', 'Stochastic Programming'), ('Multivariate Analysis', 'Multivariate Analysis'), ('Algorithms Design & Analysis', 'Algorithms Design & Analysis'), ('Time Series Analysis', 'Time Series Analysis'), ('Regression Analysis', 'Regression Analysis'), ('Non Parametric Methods', 'Non Parametric Methods'), ('Software engineering & Info processing', 'Software Engineering and Info processing'), ('System development', 'System development'), ('Computer Apps to Industry', 'Computer Apps to Industry'), ('Database design & implementation', 'Database design & implementation'), ('Data Communication Networks', 'Data Communication Networks'), ('Computer & library service', 'Computer & library service'), ('Academic Libraries Administration', 'Academic Libraries Administration'), ('Public Libraries Administration', 'Public Libraries Administration'), ('Archives $ Records Administration', 'Archives $ Records Administration')], max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='rating',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitallibrary.Student'),
        ),
        migrations.AddIndex(
            model_name='rating',
            index=models.Index(fields=['student', 'item'], name='digitallibr_student_cb3ad0_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('student', 'item')},
        ),
    ]
