from django.contrib import admin
from .models import ContestName,Contestent,Team,TeamContestent
# Register your models here.
@admin.register(ContestName)
class ContestNameAdmin(admin.ModelAdmin):
    list_display = ['contest_name']

@admin.register(Contestent)
class ContestentAdmin(admin.ModelAdmin):
    list_display = ['roll_no','reg_no','full_name']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name','department','contest_type']

@admin.register(TeamContestent)
class TeamContestentAdmin(admin.ModelAdmin):
    list_display = ['team','contestent']