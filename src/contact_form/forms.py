from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
