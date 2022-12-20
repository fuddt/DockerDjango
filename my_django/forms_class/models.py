from django.db import models

# Create your models here.
class PokemonInfo(models.Model):
    trainers_name = models.CharField(max_length=8)
    pokemons_name = models.CharField(max_length=6)
    pokemons_level = models.IntegerField(default=1)
    self_intro = models.CharField(max_length=150)
    
    def __str__(self):
        return 'trainers_id: ' + str(self.id) + ',' +\
                'trainers_name: ' + str(self.trainers_name) + ',' +\
                'pokemons_name: ' + str(self.pokemons_name) + ',' +\
                'pokemons_level:' + str(self.pokemons_level) + ',' +\
                'self_introduction:' + str(self.self_intro)
    