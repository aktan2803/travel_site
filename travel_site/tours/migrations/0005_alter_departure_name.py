from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_tour_nights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departure',
            name='name',
            field=models.CharField(choices=[('Из Москвы', 'Из Москвы'), ('Из Петербурга', 'Из Петербурга'), ('Из Новосибирска', 'Из Новосибирска'), ('Из Екатеринбурга', 'Из Екатеринбурга'), ('Из Казани', 'Из Казани')], max_length=50, verbose_name='Город отправления'),
        ),
    ]
