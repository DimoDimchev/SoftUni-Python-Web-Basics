from django import forms


class TodoForm(forms.Form):
    def __init__(self):
        super().__init__()
        for (field_name, field) in self.fields.items():
            if 'class' in field.widget.attrs:
                value = field.widget.attrs['class'] + ' form-control'
            else:
                value = ' form-control'
            field.widget.attrs['class'] = value

    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': '',
    }), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': '',
    }), required=False)
