from django import forms

class studentLoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Please Enter Your Enrollment Number'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Please Enter Your Password'}
        )
    )