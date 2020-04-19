# Generated by Django 2.2.9 on 2020-04-19 17:49

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments', validators=[utils.validators.validate_file_size]),
        ),
    ]