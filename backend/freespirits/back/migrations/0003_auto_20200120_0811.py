# Generated by Django 3.0 on 2020-01-20 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_auto_20200120_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='back.Cat', verbose_name='Cat'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='back.Cat', verbose_name='Cat'),
        ),
    ]