from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import CitationForm
from .models import Citation


class CitationList(generic.ListView):
    model = Citation

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Citation.objects.filter(user=self.request.user)


class CitationCreate(generic.CreateView):
    model = Citation
    form_class = CitationForm
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CitationUpdate(generic.UpdateView):
    model = Citation
    form_class = CitationForm
    template_name_suffix = '_update_form'

    def get_queryset(self):
        return Citation.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Citation Updated Successfully')
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CitationDetail(generic.DetailView):
    model = Citation
    slug_field = 'slug'

    def get_queryset(self):
        return Citation.objects.filter(user=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CitationDelete(generic.DeleteView):
    model = Citation
    success_url = reverse_lazy('citation:list')

    def get_queryset(self):
        return Citation.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Citation Deleted')
        return super().delete(request, *args, **kwargs)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
