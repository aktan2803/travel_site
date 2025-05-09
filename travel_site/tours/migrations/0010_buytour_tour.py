from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_remove_buytour_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='buytour',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tours.tour', verbose_name='Выбранный тур'),
        ),
    ]
