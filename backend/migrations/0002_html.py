# Generated by Django 2.1.1 on 2018-08-31 21:51

import backend.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Html',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature_code', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=256)),
                ('html_code', models.TextField()),
                ('count', models.IntegerField()),
                ('category', models.CharField(max_length=256)),
                ('code_type', models.CharField(max_length=32)),
                ('created_at', models.FloatField(default=backend.models.get_created_at)),
                ('updated_at', models.FloatField(default=backend.models.get_created_at)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='signatures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]