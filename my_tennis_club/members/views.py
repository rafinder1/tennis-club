"""
This module contains views for handling requests related to members.
It includes views for displaying a list of all members, displaying
details of a specific member, and rendering the main page.
"""

from django.http import HttpResponse
from django.template import loader

from .models import Member


def members(request):
    """
    View to display a list of all members.
    Retrieves all members from the database and renders the 'all_members.html' template.
    """
    my_members = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers": my_members,
    }
    return HttpResponse(template.render(context, request))


def details(request, member_id):
    """
    View to display details of a specific member.
    Retrieves the member with the provided ID and renders the 'details.html' template.

    :param member_id: The ID of the member whose details to display.
    """
    my_member = Member.objects.get(id=member_id)
    template = loader.get_template("details.html")
    context = {
        "mymember": my_member,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    """
    View to render the main page.
    Retrieves and renders the 'main.html' template.
    """
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
