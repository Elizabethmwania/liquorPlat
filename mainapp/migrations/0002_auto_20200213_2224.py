# Generated by Django 2.2.9 on 2020-02-13 19:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description',
        ),
        migrations.RemoveField(
            model_name='products',
            name='is_instock',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.CreateModel(
            name='Liqs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_instock', models.BooleanField(default=True)),
                ('img', models.ImageField(upload_to='media')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Brands')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Products')),
            ],
        ),
        migrations.AddField(
            model_name='brands',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Products'),
        ),
    ]
