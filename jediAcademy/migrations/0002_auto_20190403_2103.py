# Generated by Django 2.2 on 2019-04-03 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jediAcademy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='jedi',
            options={'verbose_name': 'Джедай', 'verbose_name_plural': 'Джедаи'},
        ),
        migrations.AlterModelOptions(
            name='padawantest',
            options={'verbose_name': 'Тестовое испытание падавана', 'verbose_name_plural': 'Тестовое испытания падаванов'},
        ),
        migrations.AlterModelOptions(
            name='planet',
            options={'verbose_name': 'Планета', 'verbose_name_plural': 'Планеты'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
    ]
