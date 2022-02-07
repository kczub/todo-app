from django import forms

from todo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ['user', 'slug', 'timestamp', 'updated']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'cols': 40
            }),
            'future_date': forms.DateInput(attrs={
                'type': 'date',
            })
        }

    # def clean(self):
    #     data = self.cleaned_data
    #     title = data.get('title')
    #     content = data.get('content')
    #     # future_date = data.get('future_date')

    #     # qs = Todo.objects.filter(title__icontains=title)
    #     # if qs.exists():
    #     #     self.add_error('title', f"\"{title}\" already exists.") # field error - better for specific fields
    #     if 'dupa' in title.lower() or 'dupa' in content.lower():
    #         raise forms.ValidationError("\"Dupa\" is not allowed") # nonfield error - error for the entire form
    #     return data