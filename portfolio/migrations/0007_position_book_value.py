# Generated by Django 2.2.1 on 2019-07-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20190704_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='book_value',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]
