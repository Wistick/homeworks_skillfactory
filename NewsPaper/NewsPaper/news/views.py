from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post
from .filters import PostFilter
from .forms import PostForm

from datetime import datetime


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['value1'] = None
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostDetailView(DetailView):
    template_name = 'flatpages/post_detail.html'
    queryset = Post.objects.all()


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'flatpages/post_create.html'
    form_class = PostForm
    login_url = '/accounts/login'
    permission_required = 'news.add_post'
    model = Post
    queryset = Post.objects.all()


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'flatpages/post_create.html'
    form_class = PostForm
    permission_required = 'news.change_post'
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'flatpages/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = 'news.delete_post'


class PostPageFilter(ListView):
    model = Post
    template_name = 'flatpages/post_search.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context
