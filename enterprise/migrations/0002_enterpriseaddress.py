# Generated by Django 3.2.13 on 2022-06-13 03:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnterpriseAddress',
            fields=[
                ('enterprise_address_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('pincode', models.BigIntegerField()),
                ('second_line_address', models.CharField(blank=True, max_length=250, null=True)),
                ('first_line_address', models.CharField(max_length=250)),
                ('landmark', models.CharField(max_length=250)),
                ('phone_number', models.BigIntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.DO_NOTHING, related_name='enterprise_address_created_by', to=settings.AUTH_USER_MODEL)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise.enterprise')),
                ('modified_by', models.ForeignKey(db_column='modified_by', on_delete=django.db.models.deletion.DO_NOTHING, related_name='enterprise_address_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
