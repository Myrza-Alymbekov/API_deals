# Generated by Django 4.2.4 on 2023-08-31 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Имя покупателя')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Gem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Камень',
                'verbose_name_plural': 'Камни',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Сумма сделки')),
                ('quantity', models.IntegerField(verbose_name='Количество камней')),
                ('date', models.DateTimeField(verbose_name='Дата и время сделки')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer', verbose_name='Клиент')),
                ('gem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gem', verbose_name='Камень')),
            ],
            options={
                'verbose_name': 'Сделка',
                'verbose_name_plural': 'Сделки',
            },
        ),
    ]
