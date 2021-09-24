from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# import requests

# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    field_id = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    owner_org = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    notes = models.CharField(max_length=500)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.field_id)

class Referee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    referee_id = models.IntegerField(blank=False, null=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.referee_id)


class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    school_id = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.school_id)

# We need to break out coach later as separate class
# How would we limit coach to only populating their teams otherwise?
class Team(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='team')
    name = models.CharField(max_length=50)
    team_id = models.IntegerField(blank=False, null=False)
    # MSA spreadsheet describes option for team pic in overview tab
    # If a picture is provided set team_picture flag true
    # Pic upload feature needed to support upload of the pic
    team_picture = models.BooleanField()
    # Will default to the admin user id
    coach_uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default=1)
    coach = models.CharField(max_length=50)
    coach_email = models.CharField(max_length=200)
    coach_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.school_id)

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.team_id)

class Match(models.Model):
    match_id = models.IntegerField(blank=False, null=False)
    home_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='home_team')
    guest_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='guest_team')
    field = models.ForeignKey(Field, on_delete=models.DO_NOTHING, related_name='field')
    referee = models.ForeignKey(Referee, on_delete=models.DO_NOTHING, related_name='referee')
    start_time = models.DateTimeField(default=timezone.now)
    match_date = models.DateField()
    home_team_score = models.IntegerField(default=0)
    guest_team_score = models.IntegerField(default=0)
    # Note-allow misc notes for capturing things such as red cards to players
    match_notes = models.CharField(max_length=200, blank=True)
    match_players_goals_scored = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.match_id)

