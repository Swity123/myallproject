# Generated by Django 3.2.9 on 2021-11-27 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_type', models.CharField(max_length=30)),
                ('special', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='watch',
            name='watch_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='watch.category'),
        ),
    ]
