# Generated by Django 5.1.3 on 2025-03-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_alter_tbl_batch_batch_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_content', models.CharField(max_length=50)),
                ('notification_date', models.CharField(max_length=50)),
            ],
        ),
    ]
