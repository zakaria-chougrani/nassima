from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from members.models import MyUser


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type': 'text',
            'required': '',
            'name': 'username',
            'id': 'username',
            'class': 'form-control',
            'placeholder': 'username',
            'maxlength': '16',
            'minlength': '4',

        })
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'required': '',
            'name': 'email',
            'id': 'email',
            'class': 'form-control',
            'placeholder': 'exemple@gmail.com',
        })
        self.fields['password1'].widget.attrs.update({
            'type': 'password',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'class': 'form-control',
            'placeholder': 'mot de passe',
            'maxlength': '22',
            'minlength': '4',
        })
        self.fields['password2'].widget.attrs.update({
            'type': 'password',
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'class': 'form-control',
            'placeholder': 'Confirmation mot de passe',
            'maxlength': '22',
            'minlength': '4',
        })

    email = forms.EmailField(max_length=60, help_text='Obligatoire. Ajoutez une adresse email valide.')

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type': 'text',
            'required': '',
            'name': 'username',
            'id': 'username',
            'class': 'form-control form-control-lg',
            'placeholder': 'username',
            'maxlength': '16',
            'minlength': '4',

        })
        self.fields['password'].widget.attrs.update({
            'type': 'password',
            'required': '',
            'name': 'password',
            'id': 'password',
            'class': 'form-control form-control-lg',
            'placeholder': 'mot de passe',
            'maxlength': '22',
            'minlength': '4',
        })
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Identifiant invalide ! ")
