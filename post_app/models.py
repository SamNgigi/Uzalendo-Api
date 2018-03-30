from django.conf import settings
from django.db import models

# Importing validators
from .validators import validate_content
# Create your models here.


class Post(models.Model):
    # Supposedly a much more robust way if defuning the user model.
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=155, validators=[validate_content])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        """
        What this function does is define a string representation of
        Post instance on the database./admin

        So instead of displaying 'Post object', what it we would see
        instead is the actual content that was recieved as input.
        """
        return str(self.content)

    """
    - Validation inside the model. Appears on whole model and is not
    specific to a field

    def clean(self, *args, **kwargs):
        content = self.content
        if content == 'abc':
            raise ValidationError(
                "
                Hi! Sorry, cannot be ABC.
                But on the bright side your validation is working
                ")
        return super(Post, self).clean(*args, **kwargs)
    """
