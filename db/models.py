from django.db import models

class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    
class ItemClass(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(db_index=True)
    
class BaseItemType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(db_index=True)
    item_class = models.ForeignKey(ItemClass)
    
class ItemExperiencePerLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    base_item_type = models.ForeignKey(BaseItemType)
    level = models.IntegerField()
    experience = models.BigIntegerField()

class Quest(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(db_index=True)
    
class QuestState(models.Model):
    id = models.IntegerField(primary_key=True)
    quest = models.ForeignKey(Quest)
    message = models.TextField()
    text = models.TextField()
    
class QuestReward(models.Model):
    id = models.IntegerField(primary_key=True)
    base_item_type = models.ForeignKey(BaseItemType)
    quest = models.ForeignKey(Quest)
    character = models.ForeignKey(Character)
    difficulty = models.IntegerField()

class ActiveSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    image = models.TextField()

class Mod(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    domain = models.IntegerField()
    generation_type = models.IntegerField()
    key = models.TextField()
    level = models.IntegerField()
    
class Stat(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.TextField()
    text = models.TextField()
    
class ModStat(models.Model):
    index = models.IntegerField()
    mod = models.ForeignKey(Mod)
    stat_min = models.IntegerField()
    stat_max = models.IntegerField()
    stat = models.ForeignKey(Stat, null=True)

class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    key = models.TextField(db_index=True)
    
class ModTag(models.Model):
    mod = models.ForeignKey(Mod)
    tag = models.ForeignKey(Tag)
    
class Meta(models.Model):
    key = models.TextField(primary_key=True)
    value = models.TextField()

class GrantedEffectsPerLevel(models.Model):
    activeskill = models.ForeignKey(ActiveSkill)
    level = models.IntegerField()

class GrantedEffectsPerLevelStat(models.Model):
    granted_effects_per_level = models.ForeignKey(GrantedEffectsPerLevel)
    index = models.IntegerField()
    value = models.IntegerField()
    stat = models.ForeignKey(Stat, null=True)
    class Meta:
        ordering = ['index']
