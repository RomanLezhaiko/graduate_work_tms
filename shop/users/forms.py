from django import forms
from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from .models import CustomUser  
  

class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    
    
    class Meta:  
        model = CustomUser  
        fields = ('username', 'email', 'password1', 'password2')  


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.name.title()