# Generated by Django 3.1.3 on 2022-10-29 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gan_dm', '0008_resultdataset_res_process_finished_yn'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultdataset',
            name='res_dataset_zip_path',
            field=models.CharField(default='', max_length=500),
        ),
    ]
