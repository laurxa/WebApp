from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import login
from django.contrib.auth import authenticate, login as login_user
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator


@user_passes_test(lambda u: not u.is_authenticated,
                  login_url='/',
                  redirect_field_name=None)
def custom_login(request, *args, **kwargs):
    return login(request, *args, **kwargs)


class Register(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password']
    template_name = 'registration/register.html'

    def form_valid(self, form):
        _ = User.objects.create_user(
            username=form.data['username'],
            password=form.data['password'],
            first_name=form.data['first_name'],
            last_name=form.data['last_name'],
        )

        user = authenticate(username=form.data['username'], password=form.data['password'])
        login_user(self.request, user)
        return HttpResponseRedirect('/')

    @method_decorator(user_passes_test(lambda u: not u.is_authenticated,
                                       login_url='/',
                                       redirect_field_name=None))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
