# Generated by Django 3.2.7 on 2021-10-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('contact', models.IntegerField(default=0)),
                ('blood', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(default='', max_length=254)),
                ('firstname', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
