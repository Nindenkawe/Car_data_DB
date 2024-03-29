# Generated by Django 4.0.1 on 2022-04-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ihute_on_off_street', '0011_rename_provider_id_provider_provider_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='vin_number',
            new_name='chassis_number',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='number_of_seats',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='use_of_vehicule',
            field=models.CharField(choices=[('Drive & Business', 'Drive & Business'), ('Transport of goods', 'Transport of goods'), ('Transport of Fuel', 'Transport of Fuel'), ('Taxi', 'Taxi')], default=1, max_length=32),
            preserve_default=False,
        ),
    ]
