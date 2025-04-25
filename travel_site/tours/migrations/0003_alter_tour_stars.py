from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_departure_slug_tour_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='stars',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default='OS', max_length=5, verbose_name='Кол-во звёзд'),
        ),
    ]
