# Generated by Django 4.1.3 on 2022-12-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainers_name', models.CharField(max_length=8)),
                ('pokemon_name', models.CharField(max_length=6)),
                ('pokemons_level', models.IntegerField(default=1)),
                ('self_intro', models.CharField(max_length=150)),
            ],
        ),
    ]
