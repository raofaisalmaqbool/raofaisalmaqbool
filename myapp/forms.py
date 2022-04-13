from dataclasses import field
from django import forms
from.models import User

class Add_Student(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']