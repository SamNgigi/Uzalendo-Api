from django.core.exceptions import ValidationError


def validate_content(value):
    """
    To customize later so as to not be able to post any profanities
    """
    content = value
    if content == 'abc':
        raise ValidationError(
            """
            Hi! Sorry, content have profanity.
            But on the bright side your validation is working!
            """)
    return value
