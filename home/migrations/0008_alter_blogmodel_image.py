# Generated by Django 5.0.2 on 2024-02-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(upload_to='blog_image'),
        ),
    ]
