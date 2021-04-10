from django.contrib import admin

from .models import Ability
from .models import Team
from .models import Costume
from .models import Weapon
from .models import Hero

admin.site.register(Ability)
admin.site.register(Team)
admin.site.register(Costume)
admin.site.register(Weapon)
admin.site.register(Hero)
