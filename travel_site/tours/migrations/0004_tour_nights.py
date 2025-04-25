from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_alter_tour_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='nights',
            field=models.PositiveIntegerField(null=True, verbose_name='Кол-во ночей'),
        ),
    ]
