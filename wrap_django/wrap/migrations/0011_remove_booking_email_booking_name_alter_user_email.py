# Generated by Django 4.0.4 on 2023-03-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0010_rename_uid_booking_user_booking_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
