from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
