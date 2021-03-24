from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post
from .filters import PostFilter
from .forms import PostForm

from datetime import datetime


class PostList(ListView):
    model = Post
    template_name = 'news.html'
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
    template_name = 'new.html'
    context_object_name = 'new'


class PostDetailView(DetailView):
    template_name = 'flatpages/post_detail.html'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'flatpages/post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'flatpages/post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'flatpages/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class PostPageFilter(ListView):
    model = Post
    template_name = 'flatpages/post_search.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


