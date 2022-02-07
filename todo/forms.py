from django import forms

from todo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = ['user', 'title', 'content', 'future_date']
        exclude = ['user', 'timestamp', 'updated']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        content = data.get('content')
        # future_date = data.get('future_date')

        # qs = Todo.objects.filter(title__icontains=title)
        # if qs.exists():
        #     self.add_error('title', f"\"{title}\" already exists.") # field error - better for specific fields
        if 'dupa' in title.lower() or 'dupa' in content.lower():
            raise forms.ValidationError("\"Dupa\" is not allowed") # nonfield error - error for the entire form
        return data