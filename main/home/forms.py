from django import forms
from .models import OrganizationalMember


class ImageForm(forms.ModelForm):
    class Meta:
        model = OrganizationalMember
        fields = ('title', 'image')