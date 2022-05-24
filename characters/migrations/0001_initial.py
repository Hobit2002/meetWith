# Generated by Django 4.0 on 2022-04-28 09:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timesLinked', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('character', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='characters.character')),
            ],
        ),
    ]
