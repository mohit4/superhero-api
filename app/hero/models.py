from django.db import models


class TimeStampedModel(models.Model):
    """Abstract model for storing time fields"""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ability(models.Model):
    """Details of a superhero ability"""

    ability = models.CharField(max_length=100)
    description = models.TextField()
    origin = models.CharField(max_length=100)

    def __str__(self):
        return self.ability


class Team(models.Model):
    """Details of a superhero team"""

    name = models.CharField(max_length=100)
    motive = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    """Details of a weapon"""

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Costume(models.Model):
    """Details of a superhero costume"""

    top = models.CharField(max_length=100)
    top_color = models.CharField(max_length=100)
    bottom = models.CharField(max_length=100)
    bottom_color = models.CharField(max_length=100)

    cape = models.BooleanField()
    cape_color = models.CharField(max_length=100, null=True, blank=True)

    mask = models.BooleanField()
    mask_color = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        mask = f"{self.mask_color} colored mask" if self.mask else "no mask"
        cape = f"{self.cape_color} colored cape" if self.cape else "no cape"
        return f"Wears a {self.top_color} {self.top}, {self.bottom_color} {self.bottom} with {mask} and {cape}"


class Hero(TimeStampedModel):
    """All the hero details"""

    name = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100)
    aliases = models.CharField(max_length=200)
    
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE, related_name='wearer')

    weapons = models.ManyToManyField(Weapon)
    abilities = models.ManyToManyField(Ability)
    affiliations = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='members', null=True)

    def __str__(self):
        return self.name
