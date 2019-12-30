from django import forms
from django.core import validators

class FormName(forms.Form):



    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean = super().clean()

        email = all_clean.get('email')
        verif_email = all_clean.get('verify_email')

        if email != verif_email:
            raise forms.ValidationError("Email doesn't match")


