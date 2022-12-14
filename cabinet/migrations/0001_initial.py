# Generated by Django 4.1 on 2022-08-25 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sur_name', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='inst_image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.author')),
            ],
        ),
        migrations.CreateModel(
            name='HastTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=200)),
                ('author', models.ManyToManyField(related_name='a_h', to='cabinet.author')),
            ],
        ),
    ]
