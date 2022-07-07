import logging
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from profileapp.models import ProfileModel


def user_created_handler(instance, created, **kwargs):
    """
    Creation of the profile model after user registers
    """
    if kwargs['raw']:
        return
    logging.info(created)
    if created:
        profile = ProfileModel(user=instance)
        profile.save()
    else:
        # Do logic in case of updating user profile
        pass

post_save.connect(user_created_handler, sender=User)