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
        return Citation.objects.filter(user=self.request.user)


class CitationCreate(generic.CreateView):
    model = Citation
    fields = ['title', 'content']
    template_name_suffix = '_create_form'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CitationUpdate(generic.UpdateView):
    model = Citation
    fields = ['title', 'content',]
    template_name_suffix = '_update_form'


class CitationDetail(generic.DetailView):
    model = Citation
    slug_field = 'slug'
