# Generated by Django 3.2 on 2022-01-23 21:30

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220123_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_date',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='updated_at',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='created_date',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
    ]