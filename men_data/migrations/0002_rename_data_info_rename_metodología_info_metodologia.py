from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('men_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Data',
            new_name='Info',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='metodología',
            new_name='metodologia',
        ),
    ]
