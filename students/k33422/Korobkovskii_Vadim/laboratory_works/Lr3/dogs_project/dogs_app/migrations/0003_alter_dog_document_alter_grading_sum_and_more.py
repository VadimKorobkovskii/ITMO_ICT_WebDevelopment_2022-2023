# Generated by Django 4.1.4 on 2022-12-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs_app', '0002_alter_club_club_email_alter_club_club_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='document',
            field=models.CharField(max_length=20, unique=True, verbose_name='Номер документа о родословной/Number of the pedigree document'),
        ),
        migrations.AlterField(
            model_name='grading',
            name='sum',
            field=models.IntegerField(blank=True, verbose_name='Сумма оценок/Grades summary'),
        ),
        migrations.AlterUniqueTogether(
            name='dogparticipation',
            unique_together={('show_dog', 'participant_dog')},
        ),
        migrations.AlterUniqueTogether(
            name='expertparticipation',
            unique_together={('show_exp_number', 'show_exp')},
        ),
    ]
