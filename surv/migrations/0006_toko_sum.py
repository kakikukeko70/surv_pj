# Generated by Django 4.0 on 2022-02-16 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surv', '0005_alter_answer_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='toko',
            name='sum',
            field=models.IntegerField(default=0),
        ),
    ]
