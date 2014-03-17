from django.db import models
from django.contrib.auth.models import User
from plugin.usermanagement.seed import AGE_RANGE, GENDER, CURRENCY

class UserProfile(models.Model):

    # General metadata
    user = models.ForeignKey(User, unique=True) # Foreign key relation to User table
    gender = models.CharField(max_length=10, choices=GENDER)
    age_range = models.CharField(max_length=25, choices=AGE_RANGE)
    birthday_date = models.DateField(blank=True, null=True)
    email = models.CharField(max_length = 100, blank=True, null=True)
    languages = models.CharField(max_length = 100, blank=True, null=True)

    # Personal Metadata
    about_me = models.TextField(blank=True, null=True) # Text field to maintain user information
    activities = models.TextField(blank=True, null=True) # Text field to maintain user information
    affiliations = models.TextField(blank=True, null=True) # Text field to maintain user information
    currency = models.CharField(max_length = 250, blank=True, null=True, choices=CURRENCY)
    quotes = models.TextField()
    website = models.CharField(max_length = 100, blank=True, null=True)

    # Address Metadata
    current_address = models.TextField(blank=True, null=True)
    current_location = models.CharField(max_length = 100, blank=True, null=True)
    hometown_location = models.CharField(max_length = 100, blank=True, null=True)

    # Education and work
    education = models.CharField(max_length = 250, blank=True, null=True)
    education_history  = models.CharField(max_length = 100, blank=True, null=True)
    work = models.CharField(max_length = 100, blank=True, null=True)

    # Control metadata
    is_blocked = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    profile_url = models.CharField(max_length = 100, blank=True, null=True)
    timezone = models.CharField(max_length = 100, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)

    def __unicode__(self):
        return u'%s' % self.user.username

from django.db.models.signals import post_save
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)