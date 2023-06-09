# Generated by Django 4.2.1 on 2023-05-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motion_app', '0003_proect_rename_customers_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='image/client', verbose_name='Фотография')),
                ('title_ru_name', models.TextField(blank=True, null=True, verbose_name='Описание имена')),
                ('designer', models.CharField(max_length=32, verbose_name='Дизайнер')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Whatsapp')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin')),
            ],
            options={
                'verbose_name': 'Наша комадна',
                'verbose_name_plural': 'Наша комадна',
                'db_table': 'Our team',
            },
        ),
    ]
