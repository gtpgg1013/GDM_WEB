# Generated by Django 3.2.16 on 2022-11-12 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gan_dm', '0011_resultdataset_res_dataset_trial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainDatasetDefect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds_image_class_num', models.CharField(max_length=50)),
                ('ds_image_class_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gan_dm.traindataset')),
            ],
        ),
    ]
