from django.views.generic import TemplateView


class Login(TemplateView):
    template_name = 'auth/login.html'
