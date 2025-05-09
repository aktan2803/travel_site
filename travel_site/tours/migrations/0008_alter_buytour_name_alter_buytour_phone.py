from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_alter_destination_options_buytour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buytour',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='buytour',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='Номер телефона'),
        ),
    ]
