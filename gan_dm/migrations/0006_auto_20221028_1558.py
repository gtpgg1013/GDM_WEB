# Generated by Django 3.1.3 on 2022-10-28 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gan_dm', '0005_traindataset_dataset_num_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traindataset',
            name='dataset_num_classes',
            field=models.IntegerField(default=1),
        ),
    ]