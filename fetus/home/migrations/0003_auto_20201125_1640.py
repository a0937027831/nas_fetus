# Generated by Django 3.0.11 on 2020-11-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201110_1050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ('-updated_at',)},
        ),
        migrations.AddField(
            model_name='banner',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='更新日期'),
        ),
    ]
