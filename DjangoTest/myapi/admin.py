from django.contrib import admin
from myapi.models import Hero
from myapi.models import Monster

# Register your models here.
admin.site.register(Monster)
admin.site.register(Hero)