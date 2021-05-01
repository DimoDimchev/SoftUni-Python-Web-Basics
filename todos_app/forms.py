from django import forms


def min_validator(value):
    if not value or len(value) < 10:
        raise forms.ValidationError(f"Value should be more than 10 characters. Now it is {len(value)}")


class TodoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
    }), validators=(min_validator,), required=False)
