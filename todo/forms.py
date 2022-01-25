from django import forms

class TodoForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data['title']
        content = cleaned_data['content']
        if title.lower().strip() == 'activity':
            self.add_error('title', "This title is taken") # field error - better for specific fields
        if 'dupa' in title.lower() or 'dupa' in content.lower():
            raise forms.ValidationError('"Dupa" is not allowed') # nonfield error - error for the entire form
        return cleaned_data