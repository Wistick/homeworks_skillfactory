from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BasicSignupForm
from news.models import Author
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect


class BaseRegisterView(CreateView):
    model = User
    form_class = BasicSignupForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        author_group.user_set.add(user)
        Author.objects.create(author_user=user)
    return redirect('/')
