from django.utils import timezone
from django import forms

from todo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ['user', 'timestamp', 'updated', 'completed']
        widgets = {
            'future_date': forms.DateInput(attrs={
                'type': 'date'
            })
        }
        # labels = {
        #     'title': ''
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'max. 30 characters',
            'class': 'form-title'
        })
        self.fields['content'].widget.attrs.update({
            'rows': 10,
            'cols': 40,
            'class': 'form-content'
        })

    def clean(self):
        data = self.cleaned_data
        future_date = data.get('future_date')
        if future_date < timezone.now().date():
            self.add_error('future_date', "Date cannot be in the past.")
        return data
    

    #     content = data.get('content')
    #     # qs = Todo.objects.filter(title__icontains=title)
    #     # if qs.exists():
    #     #     self.add_error('title', f"\"{title}\" already exists.") # field error - better for specific fields
    #     if 'dupa' in title.lower() or 'dupa' in content.lower():
    #         raise forms.ValidationError("\"Dupa\" is not allowed") # nonfield error - error for the entire form
    #     return data