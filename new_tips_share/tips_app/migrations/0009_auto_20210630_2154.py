# Generated by Django 2.2 on 2021-06-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips_app', '0008_auto_20210630_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='total_hours',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pool',
            name='total_tips',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='hours_worked',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tips_shared',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]