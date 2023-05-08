from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ies', models.TextField()),
                ('sector_ies', models.TextField()),
                ('caracter_ies', models.TextField()),
                ('departamento_domicilio_ies', models.TextField()),
                ('municipio_domicilio_ies', models.TextField()),
                ('programa_academico', models.TextField()),
                ('nivel_academico', models.TextField()),
                ('nivel_formacion', models.TextField()),
                ('metodología', models.TextField()),
                ('sexo', models.TextField()),
                ('anio', models.TextField()),
                ('semestre', models.IntegerField()),
                ('graduados', models.TextField()),
                ('matriculados', models.IntegerField()),
            ],
        ),
    ]
