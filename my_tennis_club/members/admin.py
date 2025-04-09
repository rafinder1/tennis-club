"""Admin configuration for the members app."""

from django.contrib import admin

from .models import Member


class MemberAdmin(admin.ModelAdmin):
    """Admin interface options for the Member model."""

    list_display = (
        "firstname",
        "lastname",
        "joined_date",
    )


admin.site.register(Member, MemberAdmin)
