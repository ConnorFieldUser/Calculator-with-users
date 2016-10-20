from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

# from django.contrib.auth.models import User

# Create your models here.


POSSIBLE_OPS = [
    ('+', '+'),
    ('-', '-'),
    ('*', '*'),
    ('/', '/'),
]


class Operation(models.Model):
    created_by = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    operator = models.CharField(max_length=1)
    description = models.TextField(null=True, blank=True)

    @property
    def do_the_math(self):
        operator, num1, num2 = [self.operator, self.num1, self.num2]
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        else:
            return num1 / num2


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
