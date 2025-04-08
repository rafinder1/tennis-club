"""
This module defines the URL patterns for the application.
It includes paths for the main page, member listing, and member details.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("members/", views.members, name="members"),
    path("members/details/<int:id>", views.details, name="details"),
]
