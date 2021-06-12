# Generated by Django 3.2.4 on 2021-06-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mail',
            field=models.EmailField(default='NA', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
