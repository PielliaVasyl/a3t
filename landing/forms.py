from django import forms
from landing.models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ["name", "email", "tel", "company_title", "company_edrpou"]
