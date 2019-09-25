from django import forms

class ListingForm(forms.Form):
    Name = forms.CharField(max_length=100)
    email = forms.EmailField()
    price = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)