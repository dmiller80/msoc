from django.contrib import admin
from .models import School, Team, Player, Field, Referee, Match

class FieldList(admin.ModelAdmin):
    list_display = ('field_id', 'name', 'owner_org', 'phone')
    list_filter = ('field_id', 'name', 'owner_org')
    search_fields = ('field_id', 'name')
    ordering = ['field_id']

class RefereeList(admin.ModelAdmin):
    list_display = ('referee_id', 'last_name', 'first_name', 'phone', 'email')
    list_filter = ('last_name', 'email')
    search_fields = ('Last_name', 'email')
    ordering = ['last_name']

class MatchList(admin.ModelAdmin):
    list_display = ('match_id', 'home_team', 'match_date', 'field')
    list_filter = ('match_id', 'home_team', 'match_date')
    search_fields = ('match_id', 'date')
    ordering = ['match_id']

class SchoolList(admin.ModelAdmin):
    list_display = ('school_id', 'name', 'contact', 'phone')
    list_filter = ('school_id', 'name', 'contact')
    search_fields = ('school_id', 'name')
    ordering = ['school_id']


class TeamList(admin.ModelAdmin):
    list_display = ('school', 'name', 'coach', 'coach_phone')
    list_filter = ('school', 'name')
    search_fields = ('school', 'name')
    ordering = ['school']

class PlayerList(admin.ModelAdmin):
    list_display = ('team', 'first_name', 'last_name', 'city')
    list_filter = ('team', 'last_name')
    search_fields = ('team', 'last_name')
    ordering = ['team']

# Register your models here.


admin.site.register(School, SchoolList)
admin.site.register(Team, TeamList)
admin.site.register(Player, PlayerList)
admin.site.register(Field, FieldList)
admin.site.register(Referee, RefereeList)
admin.site.register(Match, MatchList)
