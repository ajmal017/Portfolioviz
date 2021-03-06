# Generated by Django 2.2.1 on 2019-07-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_remove_position_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='position',
            name='transaction_type',
            field=models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell')], default='BUY', max_length=4),
        ),
    ]
