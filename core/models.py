from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Profile model containing all information associated with a user.

    fields:
        user (User): user object containing all basic information related to user
        bio (text): info provided bu user about himself/herself
        gender (str): gender of user
        photo (img): image of user
        date_of_birth (date): date of birth of user
        mobile_number (number): mobile number of user
        address (str): address of user
        city (str): city of user
        country (str): country of user

    """
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        help_text='Some details about the user.', max_length=500, null=True
    )
    gender = models.CharField(
        max_length=10, help_text='Specify gender.', choices=GENDER_CHOICES, null=True
    )
    photo = models.ImageField(help_text='Profile picture.', null=True)
    date_of_birth = models.DateField(help_text='Date of birth.', null=True)
    mobile_number = models.CharField(
        help_text='Verified mobile number with country code', max_length=15, null=True
    )
    address = models.CharField(help_text='Local address of user.', max_length=250, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal function for when a default django User is created. Function is
    called after creation of User object (post_save) and proceeds to create a
    Profile object.

    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal function for when a default django User is saved. Function is called
    after saving of User object (post_save) and proceeds to update the Profile
    object.

    """
    instance.profile.save()
