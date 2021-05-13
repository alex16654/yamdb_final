from datetime import datetime

from django.core.exceptions import ValidationError


def year_validator(value):
    year_less = "Год издания не может быть меньше 1500."
    year_more = "Год издания не может быть больше текущего."
    if value < 1500:
        raise ValidationError(f'{year_less}', params={'value': value})
    if value > datetime.now().year:
        raise ValidationError(f'{year_more}', params={'value': value})
