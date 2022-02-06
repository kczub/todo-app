from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'confirm password'
            }))

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'password',
                'type': 'password'
            })
        }

    def clean(self):
        data = self.cleaned_data
        username = data.get('username')
        password1 = data.get('password')
        password2 = data.get('confirm_password')
        qs = User.objects.filter(username__icontains=username)
        if qs.exists():
            raise forms.ValidationError(f"username {username} is taken.")
        if password1 != password2:
            raise forms.ValidationError("Confirm password")
        print(data)
        return data
