from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.name.title()