from django import forms
from .models import Calendar,Schedule,CalendarUser



class CalendarForm(forms.ModelForm):
    class Meta:
        model   = Calendar
        fields  = ["name","user","share" ]


class ScheduleForm(forms.ModelForm):
    class Meta:
        model   = Schedule
        fields  = [ "calendar","start_dt","end_dt","content","user" ]

class CalendarUserForm(forms.ModelForm):
    class Meta:
        model   = CalendarUser
        fields  = [ "calendar","user","read","write","chat" ] 

