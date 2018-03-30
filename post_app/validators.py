from django.core.exceptions import ValidationError


def validate_content(value):
    # To make a vialidation appear on a specific field
    content = value
    if content == 'abc':
        raise ValidationError(
            """
            Hi! Sorry, content cannot be 'abc'.
            But on the bright side your validation is working!
            """)
    return value
