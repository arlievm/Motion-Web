# Generated by Django 4.2.1 on 2023-05-30 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motion_app', '0004_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru_tehnol', models.TextField(blank=True, null=True, verbose_name='Описание Технологии и Инструменты ')),
                ('name', models.CharField(max_length=255)),
                ('parent_instrument', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='motion_app.instruments')),
            ],
            options={
                'verbose_name': 'Технологии и Инструменты',
                'verbose_name_plural': 'Технологии и Инструменты',
                'db_table': 'technologies_and_tools',
            },
        ),
    ]
