from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

from _common.models.abstract_models import TimeStampedModel, TextAndPreviewTextModel, SlugModel


class Citation(TimeStampedModel,
               TextAndPreviewTextModel,
               SlugModel):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('citation:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
