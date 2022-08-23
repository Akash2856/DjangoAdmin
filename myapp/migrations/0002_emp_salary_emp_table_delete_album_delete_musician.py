# Generated by Django 4.1 on 2022-08-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='emp_salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.IntegerField()),
                ('emp_sal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='emp_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_first_name', models.CharField(max_length=10)),
                ('emp_last_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
    ]
