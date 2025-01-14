# Generated by Django 5.1.4 on 2025-01-14 20:06

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_author_book_bookinstance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a language for the book (e.g. French, Spanish, English etc.)', max_length=255, unique=True)),
            ],
            options={
                'constraints': [models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='language_name_case_insensitive_unique', violation_error_message='Language already exists (case insensitive match)')],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Select a language for this book', to='catalog.language'),
        ),
    ]
