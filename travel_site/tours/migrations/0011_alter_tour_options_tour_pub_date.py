from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0010_buytour_tour'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Тур', 'verbose_name_plural': 'Туры'},
        ),
        migrations.AddField(
            model_name='tour',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время публикации тура'),
            preserve_default=False,
        ),
    ]
