# Generated by Django 3.0.5 on 2020-05-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0003_episode_podcast'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='episode_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='apple_id',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='episode',
            name='spotify_id',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='episode',
            name='upload_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='youtube_id',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
