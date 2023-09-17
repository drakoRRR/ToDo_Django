from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Select
from datetime import date


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'tag', 'description', 'deadline']
        tags = ['Homework', 'Routine', 'Work', 'Relax']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Your name..'
            }),
            'tag': Select(choices=[('work', 'Work'), ('study', 'Study'), ('hobby', 'Hobby')]),
            'description': Textarea(attrs={
                'placeholder': "Write something..",
                'style': "height:200px"
            }),
            'deadline': TextInput(attrs={
                'type': 'date',
                'value': date.today()
            })
        }
