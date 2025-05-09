from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_destination_tour_destination'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destination',
            options={'verbose_name': 'Прибытие', 'verbose_name_plural': 'Прибытия'},
        ),
        migrations.CreateModel(
            name='BuyTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя покупателя')),
                ('email', models.EmailField(blank=True, max_length=120, null=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Время оформления заказа')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tours.tour', verbose_name='Выбранный тур')),
            ],
            options={
                'verbose_name': 'Заказ тура',
                'verbose_name_plural': 'Заказы туров',
                'ordering': ['-time'],
            },
        ),
    ]
