from django import forms
from .models.destination import Destination
from django.core.exceptions import ValidationError



class PublicDestinationForm(forms.ModelForm):
    geolocation = forms.CharField(label='Geolocation', widget=forms.TextInput(attrs={"placeholder": "Geolocation",
                                                                                     "class": 'form-control'}))
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Title",
                                                                         "class": 'form-control'}))
    image = forms.CharField(label='Image URL', widget=forms.TextInput(attrs={"placeholder": "Image URL",
                                                                             "class": 'form-control'}))
    description = forms.CharField(label='Description', max_length=300, widget=forms.Textarea(attrs={"placeholder": "Description",
                                                                                    "class": 'form-control'}))

    class Meta:
        model = Destination
        fields = [
            'geolocation', 'title', 'image', 'description',
        ]


class PrivateDestinationForm(forms.ModelForm):
    geolocation = forms.CharField(label='Geolocation', widget=forms.TextInput(attrs={"placeholder": "Geolocation",
                                                                                     "class": 'form-control'}))
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Title",
                                                                         "class": 'form-control'}))
    image = forms.CharField(label='Image URL', widget=forms.TextInput(attrs={"placeholder": "Image URL",
                                                                             "class": 'form-control'}))
    description = forms.CharField(label='Description', max_length=300, widget=forms.Textarea(attrs={"placeholder":
                                                                                                    "Description",
                                                                                                    "class":
                                                                                                        'form-control'
                                                                                                    }))
    departure_date = forms.DateField(label='Departure date', widget=forms.DateInput(attrs={"class": 'form-control',
                                                                                           'type': 'date'}))
    arrival_date = forms.DateField(label='Arrival date', widget=forms.DateInput(attrs={"class": 'form-control',
                                                                                       'type': 'date'}))

    def clean_arrival_date(self):
        departure_date = self.cleaned_data.get('departure_date')
        arrival_date = self.cleaned_data.get('arrival_date')

        if departure_date and arrival_date:
            if departure_date > arrival_date:
                raise ValidationError("Arrival date should be after departure date.")

        return arrival_date

    def clean_departure_date(self):
        departure_date = self.cleaned_data.get('departure_date')
        arrival_date = self.cleaned_data.get('arrival_date')

        if departure_date and arrival_date:
            if departure_date > arrival_date:
                raise ValidationError("Arrival date should be after departure date.")

        return departure_date

    class Meta:
        model = Destination
        fields = [
            'geolocation', 'title', 'image', 'description', 'departure_date', 'arrival_date'
        ]
