from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Citation


class CitationList(generic.ListView):
    model = Citation
    template_name = 'citation/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        citations = Citation.objects.filter(user=self.request.user).filter(active=True)
