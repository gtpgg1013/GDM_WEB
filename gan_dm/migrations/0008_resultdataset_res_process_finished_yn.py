# Generated by Django 3.1.3 on 2022-10-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gan_dm', '0007_auto_20221028_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultdataset',
            name='res_process_finished_YN',
            field=models.BooleanField(default=False),
        ),
    ]
