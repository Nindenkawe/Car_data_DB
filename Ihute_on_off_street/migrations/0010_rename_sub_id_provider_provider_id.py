# Generated by Django 4.0.1 on 2022-03-28 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ihute_on_off_street', '0009_alter_provider_service_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='sub_id',
            new_name='provider_id',
        ),
    ]
