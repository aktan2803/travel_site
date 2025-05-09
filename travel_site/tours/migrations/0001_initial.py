from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('bish', 'Из Бишкека'), ('ik', 'Из Каракола'), ('osh', 'Из Оша'), ('djl', 'Из Джалал-Абада'), ('tal', 'Из Таласа')], max_length=50, verbose_name='Город отправления')),
            ],
            options={
                'verbose_name': 'Отправление',
                'verbose_name_plural': 'Отправления',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Название')),
                ('description', models.TextField(max_length=6000, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('stars', models.CharField(choices=[('OS', 1), ('TWS', 2), ('THRS', 3), ('FOURS', 4), ('FIVS', 5)], default='OS', max_length=5, verbose_name='Кол-во звёзд')),
                ('departure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours', to='tours.departure', verbose_name='Город отправления')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(null=True, verbose_name='Рейтинг')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ratings', to='tours.tour')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
    ]
