# Generated by Django 4.0 on 2022-02-17 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surv', '0009_category_toko'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='toko',
            new_name='tokos',
        ),
    ]
