# Generated by Django 4.0.dev20210517092135 on 2021-06-12 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='base.genre'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='cd',
            name='genre',
        ),
        migrations.AddField(
            model_name='cd',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='base.genre'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='base.genre'),
            preserve_default=False,
        ),
    ]
