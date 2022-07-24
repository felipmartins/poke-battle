from email.policy import default
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50)
    double_damage_from = models.JSONField(default=dict)
    double_damage_to = models.JSONField(default=dict)
    half_damage_from = models.JSONField(default=dict)
    half_damage_to = models.JSONField(default=dict)
    no_damage_from = models.JSONField(default=dict)
    no_damage_to = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class Move(models.Model):
    name = models.CharField(max_length=50)
    accuracy = models.IntegerField(null=True)
    power = models.IntegerField(null=True)
    damage_class = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    sprite = models.ImageField()
    type_1 = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type1')
    type_2 = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type2')
    move_set = models.JSONField(default=dict)
    move = models.CharField(max_length=50, default='pound')
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_attack = models.IntegerField()
    speed = models.IntegerField()


