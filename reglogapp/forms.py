from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='Enter your First name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }
        )
    )

    last_name = forms.CharField(
        label='Enter your last name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'last Name'
            }
        )
    )

    username = forms.CharField(
        label='Enter user name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'user Name'
            }
        )
    )

    password = forms.CharField(
        label='Enter your password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter mobile number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'mobile number'
            }
        )
    )

    email = forms.EmailField(
        label='Enter Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Enter user name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'user Name'
            }
        )
    )

    password = forms.CharField(
        label='Enter your First name',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }
        )
    )
