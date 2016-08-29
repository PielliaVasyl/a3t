from django.contrib import admin
from landing.forms import UserProfileForm
from landing.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "tel", "company_title", "company_edrpou"]
    form = UserProfileForm

admin.site.register(UserProfile, UserProfileAdmin)
