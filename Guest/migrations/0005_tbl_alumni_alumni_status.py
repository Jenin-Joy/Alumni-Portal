# Generated by Django 5.1.3 on 2025-01-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_alter_tbl_alumni_alumni_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_alumni',
            name='alumni_status',
            field=models.IntegerField(default=0),
        ),
    ]
