# Generated by Django 5.1.3 on 2025-01-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_alter_tbl_subcategory_subcategory_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=50)),
            ],
        ),
    ]
