from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class()

    def add_form_control_class(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = ' form-control'

    class Meta:
        model = Book
        fields = '__all__'
