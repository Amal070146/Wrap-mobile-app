# Generated by Django 4.0.4 on 2023-03-26 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0011_remove_booking_email_booking_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default=1323, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
