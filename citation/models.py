from django.db import models
from django.contrib.auth.models import User

from _common.models.abstract_models import TimeStampedModel, RichTextAndPreviewTextModel, SlugModel


class Citation(TimeStampedModel,
               RichTextAndPreviewTextModel,
               SlugModel):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return NotImplementedError

    def __str__(self):
        return self.title
