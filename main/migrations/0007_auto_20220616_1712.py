# Generated by Django 3.2.12 on 2022-06-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_skill_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='date',
        ),
        migrations.AddField(
            model_name='certificate',
            name='link',
            field=models.CharField(blank=True, default='jacobmolinar.herokuapp.com', max_length=100),
        ),
    ]
