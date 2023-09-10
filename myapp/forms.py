from django import forms 
from django.contrib.auth.models import User 

"""TEACHER_GRADE_CHOICES = (
    #('PhD', 'PhD'),
    ('PR', 'PR'),
)
"""
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat', widget=forms.PasswordInput)
    #faculty = forms.CharField(label='Faculty')
    
    #teacher_grade = forms.ChoiceField(label='Teacher Grade', choices=TEACHER_GRADE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")

        return cd['password2']

