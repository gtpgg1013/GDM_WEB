# Generated by Django 3.1.3 on 2022-10-29 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gan_dm', '0009_resultdataset_res_dataset_zip_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultdataset',
            name='gen_model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gan_dm.generativemodel'),
        ),
    ]