# Generated by Django 4.1.7 on 2023-03-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=256, verbose_name='Тема заметки')),
                ('text', models.TextField(blank=True, verbose_name='Текст заметки')),
                ('image', models.ImageField(blank=True, default=None, upload_to='images/%Y/%m/%d')),
                ('soundex', models.TextField(blank=True, verbose_name='soundex(subject + text в фонетическом виде)')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
                'ordering': ['-pub_date'],
            },
        ),
    ]
