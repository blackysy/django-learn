# Generated by Django 2.2.2 on 2019-06-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
