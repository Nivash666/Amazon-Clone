# Generated by Django 4.1.4 on 2023-02-20 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0010_rename_tv_brand_tv_brand_rename_tv_os_tv_os_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shirts',
            old_name='shirt_discount',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='shirts',
            old_name='shirt_discount_price',
            new_name='discount_price',
        ),
        migrations.RenameField(
            model_name='shirts',
            old_name='shirt_head',
            new_name='head',
        ),
        migrations.RenameField(
            model_name='shirts',
            old_name='shirt_integer_dicount',
            new_name='int_dicount_price',
        ),
        migrations.RenameField(
            model_name='shirts',
            old_name='shirt_integer_orginal',
            new_name='int_orginal_price',
        ),
        migrations.RenameField(
            model_name='shirts',
            old_name='shirt_orginal_price',
            new_name='orginal_price',
        ),
    ]
