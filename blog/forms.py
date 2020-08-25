from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Search...'}
    ))


class ContactEmailForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Your Name'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': 'Your Email'}
    ))
    subject = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Your Subject'}
    ))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control',
               'name': "", 'id': '', 'cols': "30", 'rows': "7",
               'placeholder': 'Your Message'}
    ))
