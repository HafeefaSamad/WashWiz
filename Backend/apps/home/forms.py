from django import forms
from datetime import datetime,timedelta
from .models import Slot


class DateSelectionForm(forms.Form):
    # Timeslot = (
    #     (0,'9-10'),
    #     (0,'10-11'),
    #     (0,'11-12'),
    #     (0,'12-1'),
    #     (0,'2-3'),
    #     (0,'3-4'),
    #     (0,'4-5'),

    # )
    date_choices = [(datetime.today() + timedelta(days=i), (datetime.today() + timedelta(days=i)).strftime('%Y-%m-%d')) for i in range(6)]
    date = forms.DateField(widget=forms.Select(choices=date_choices))
    # slot_choices = [(slot.timeslot) for slot in Slot.objects.all()]
    # slot = forms.ChoiceField(choices=slot_choices, widget=forms.Select())
    
