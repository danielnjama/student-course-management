# Generated by Django 4.2.11 on 2024-04-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_emailtemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
