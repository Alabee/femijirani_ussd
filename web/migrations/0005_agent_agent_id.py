# Generated by Django 2.0.5 on 2018-12-12 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20181212_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='agent_id',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]