# Generated by Django 2.0.6 on 2018-06-15 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='text',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
    ]
