# Generated by Django 3.1.2 on 2020-10-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_beer_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='test1',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='test2',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='alcohol',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='ingredient',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
