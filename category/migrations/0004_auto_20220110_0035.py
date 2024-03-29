# Generated by Django 3.1.7 on 2022-01-09 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20211207_0104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی ', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='photos/categories', verbose_name='تصویر دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=255, verbose_name='توضیحات'),
        ),
    ]
