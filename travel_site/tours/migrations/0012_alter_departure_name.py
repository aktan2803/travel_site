from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0011_alter_tour_options_tour_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departure',
            name='name',
            field=models.CharField(choices=[('Из Бишкека', 'Из Бишкека'), ('Из Петербурга', 'Из Петербурга'), ('Из Новосибирска', 'Из Новосибирска'), ('Из Екатеринбурга', 'Из Екатеринбурга'), ('Из Казани', 'Из Казани')], max_length=50, verbose_name='Город отправления'),
        ),
    ]
