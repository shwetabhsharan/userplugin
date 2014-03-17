from plugin.usermanagement.models import *
from django.contrib.auth.models import User

def get_all_users():
    """
        Purpose: To return a list of user objects
        Input: NA
        Returns: User object list
        Dependency: NA
    """
    return User.objects.all()
