# Generated by Django 2.2 on 2019-08-06 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('cell', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('religion', models.CharField(max_length=50)),
                ('pic', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')),
                ('fb', models.URLField(blank=True)),
                ('insta', models.URLField(blank=True)),
                ('education_level', models.CharField(blank=True, max_length=100)),
                ('education_field', models.CharField(blank=True, max_length=200)),
                ('work_as', models.CharField(blank=True, max_length=50)),
                ('work_in', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
