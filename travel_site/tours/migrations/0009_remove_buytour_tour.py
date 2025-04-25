from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0008_alter_buytour_name_alter_buytour_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buytour',
            name='tour',
        ),
    ]
