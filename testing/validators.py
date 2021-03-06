from django.core.exceptions import ValidationError


def contains_only_digits(value):
    result = all(x.isdigit() for x in value)
    if not result:
        raise ValidationError('Egn should contain digits only')
