from random import randint
from django.db import models

def getRandomMana():
    return randint(1, 200)  

class Hero(models.Model):
    name = models.CharField(max_length=60)
    hitpoints = models.IntegerField()
    strength = models.IntegerField()
    mana = models.IntegerField(default=getRandomMana)
    gold = models.DecimalField(decimal_places=4, max_digits=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'Hero[name={self.name}, email={self.email}]'

class Monster(models.Model):
    name = models.CharField(max_length=60)
    hitpoints = models.IntegerField()
    
    def __str__(self):
        return f'Monster[name={self.name}]'



#Create Hero model with Name, HP, Gold (money), Email using appropriate fields
#Make sure you can browse from Admin interface
