# Generated by Django 3.2.9 on 2022-01-16 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw_10.city')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Towar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40)),
                ('clients', models.ManyToManyField(to='hw_10.Client')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='suppliers',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hw_10.supplier'),
        ),
    ]