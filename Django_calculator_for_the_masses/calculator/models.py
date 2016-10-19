from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

# from django.contrib.auth.models import User

# Create your models here.


class Calc(models.Model):
    created_by = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    operation = models.CharField(max_length=1)
    result = models.IntegerField()
    description = models.TextField(null=True, blank=True)

ACCESS_LEVELS = [
    ('u', 'user'),
    ('o', 'Owner'),
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

    @property
    def is_owner(self):
        return self.access_level == 'o'


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)
