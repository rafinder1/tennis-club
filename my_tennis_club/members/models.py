"""
This module contains the definition of the Member model for the MyTennisClub application.
"""

from django.db import models


class Member(models.Model):
    """
    Represents a member of the tennis club with basic information like
    first name, last name, phone number, and the date they joined.
    """

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
