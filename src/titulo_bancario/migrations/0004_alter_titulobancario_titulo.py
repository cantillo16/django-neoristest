# Generated by Django 4.1.4 on 2022-12-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titulo_bancario', '0003_alter_titulobancario_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulobancario',
            name='titulo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]