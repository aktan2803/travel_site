from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departure',
            name='slug',
            field=models.SlugField(max_length=130, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='slug',
            field=models.SlugField(max_length=130, null=True, unique=True),
        ),
    ]
