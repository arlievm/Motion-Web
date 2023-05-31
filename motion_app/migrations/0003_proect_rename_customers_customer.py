# Generated by Django 4.2.1 on 2023-05-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motion_app', '0002_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='image/client', verbose_name='Фотография')),
                ('title_ru_pro', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Наши проекты',
                'verbose_name_plural': 'Наши проекты',
                'db_table': 'Our Projects',
            },
        ),
        migrations.RenameModel(
            old_name='customers',
            new_name='Customer',
        ),
    ]
