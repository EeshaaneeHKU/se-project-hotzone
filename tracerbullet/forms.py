from django.forms import ModelForm, TextInput
from .models import UserDetails

class UserForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name']