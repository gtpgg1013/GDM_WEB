# Generated by Django 3.1.3 on 2022-10-28 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gan_dm', '0006_auto_20221028_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generativemodel',
            old_name='algorithm_name',
            new_name='algorithm',
        ),
        migrations.RenameField(
            model_name='generativemodel',
            old_name='ds_version',
            new_name='tds',
        ),
        migrations.RenameField(
            model_name='inputinferencedatasetimage',
            old_name='ii_ds_version',
            new_name='iids',
        ),
        migrations.RenameField(
            model_name='resultdatasetimage',
            old_name='res_ds_version',
            new_name='rds',
        ),
        migrations.RenameField(
            model_name='traindatasetimage',
            old_name='ds_version',
            new_name='tds',
        ),
    ]
