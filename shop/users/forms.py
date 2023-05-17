from django import forms
from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from .models import CustomUser  
  

class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200)  
    
    
    class Meta:  
        model = CustomUser  
        fields = ('username', 'email', 'password1', 'password2')  
    

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == 'password1':
                visible.field.widget.attrs['placeholder'] = 'Password'
            elif visible.name == 'password2':
                visible.field.widget.attrs['placeholder'] = 'Password confirmation'
            else:
                visible.field.widget.attrs['placeholder'] = visible.name.title()
            


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.name.title()