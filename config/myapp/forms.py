from django.contrib.auth.forms import UserCreationForm
from django import forms

from myapp.models import User,Pet

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields 
        
        
    
    
        
        

