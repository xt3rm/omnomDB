from django.contrib import admin
from .models import Food
from .models import UserGoal
from .models import JournalEntry
# Register your models here.
admin.site.register(Food)
admin.site.register(UserGoal)
admin.site.register(JournalEntry)
