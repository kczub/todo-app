from django.utils import timezone
from django import forms

from todo.models import Todo

class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'max. 30 characters'
    }))

    content = forms.CharField(widget=forms.Textarea(attrs={
            'rows': 10,
            'cols': 40
    }))

    future_date = forms.DateField(widget=forms.DateInput(attrs={
            'type': 'date'
    }))

    class Meta:
        model = Todo
        exclude = ['user', 'timestamp', 'updated', 'completed']

    def clean(self):
        data = self.cleaned_data
        future_date = data.get('future_date')
        if future_date < timezone.now().date():
            self.add_error('future_date', "Date cannot be in the past.")
        return data
    

    #     content = data.get('content')
    #     # 

    #     # qs = Todo.objects.filter(title__icontains=title)
    #     # if qs.exists():
    #     #     self.add_error('title', f"\"{title}\" already exists.") # field error - better for specific fields
    #     if 'dupa' in title.lower() or 'dupa' in content.lower():
    #         raise forms.ValidationError("\"Dupa\" is not allowed") # nonfield error - error for the entire form
    #     return data