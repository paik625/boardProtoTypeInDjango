# Generated by Django 2.1.5 on 2019-01-30 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ['create_at']},
        ),
    ]