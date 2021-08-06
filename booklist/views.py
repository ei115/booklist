from django.contrib.auth import login
from django.urls.base import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models import BookModel
from .forms import CreateForm, LoginForm, UserCreateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class OnlyYouPostMixin(UserPassesTestMixin):
    raise_exception = True
    def test_func(self):
        post = BookModel.objects.get(id = self.kwargs['pk'])
        return post.contributor == self.request.user



class Index(TemplateView):
    template_name = "booklist/index.html"
    model = BookModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = BookModel.objects.all().order_by('-created_at')
        context = {
            'object_list':object_list,
        }
        return context

class Create(LoginRequiredMixin, CreateView):
    model = BookModel
    form_class = CreateForm
    success_url = reverse_lazy('booklist:index')

    def form_valid(self, form):
        form.instance.contributor_id = self.request.user.id
        return super(Create, self).form_valid(form)

class Detail(LoginRequiredMixin, DetailView):
    template_name = "booklist/detail.html"
    model = BookModel

class Update(OnlyYouPostMixin, UpdateView):
    model = BookModel
    form_class = CreateForm
    success_url = reverse_lazy('booklist:index')

class Delete(OnlyYouPostMixin, DeleteView):
    template_name = "booklist/delete.html"
    model = BookModel
    success_url = reverse_lazy('booklist:index')

class Login(LoginView):
    template_name = "booklist/login.html"
    form_class = LoginForm

class Logout(LogoutView):
    template_name = "booklist/logout.html"

class SignUp(CreateView):
    template_name = "booklist/signup.html"
    form_class = UserCreateForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return redirect('booklist:index')