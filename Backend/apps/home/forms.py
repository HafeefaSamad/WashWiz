from django import forms
from datetime import datetime,timedelta,date
from .models import Slot


class DateSelectionForm(forms.ModelForm):
    
    date_choices = [(date.today() + timedelta(days=i), (date.today() + timedelta(days=i)).strftime('%Y-%m-%d')) for i in range(6)]
    date = forms.DateField(widget=forms.Select(choices=date_choices))
    class Meta:
        model=Slot
        fields=('date',)
    # Timeslot = (
    #     (0,'9-10'),
    #     (0,'10-11'),
    #     (0,'11-12'),
    #     (0,'12-1'),
    #     (0,'2-3'),
    #     (0,'3-4'),
    #     (0,'4-5'),

    # )
    # slot_choices = [(slot.timeslot) for slot in Slot.objects.all()]
    # slot = forms.ChoiceField(choices=slot_choices, widget=forms.Select())
    
