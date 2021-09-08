from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView

from .forms import PostForm
from .models import Group, Post


def set_pagination(request, obj_list, amount):
    paginator = Paginator(obj_list, amount)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'

    post_list = Post.objects.all()
    page_obj = set_pagination(request, post_list, 10)

    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}'

    post_list = group.posts.all()
    page_obj = set_pagination(request, post_list, 10)

    context = {
        'title': title,
        'page_obj': page_obj,
        'group': group,
    }
    return render(request, template, context)


def profile(request, username):
    template = 'posts/profile.html'
    author = get_user_model().objects.get(username=username)
    title = f'Профайл пользователя {author.get_full_name()}'

    post_list = Post.objects.filter(author=author)
    page_obj = set_pagination(request, post_list, 10)

    context = {
        'title': title,
        'page_obj': page_obj,
        'author': author,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    specific_post = get_object_or_404(Post, pk=post_id)
    title = f'Пост {specific_post.text[0:30]}'

    post_list = Post.objects.filter(author=specific_post.author)
    page_obj = set_pagination(request, post_list, 10)

    context = {
        'title': title,
        'post': specific_post,
        'page_obj': page_obj,
    }
    return render(request, template, context)


@method_decorator(login_required, name='dispatch')
class post_create(CreateView):
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = '/profile/<username>'

    def get_context_data(self, **kwargs):
        context = super(post_create, self).get_context_data(**kwargs)
        context['is_edit'] = False
        return context

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        form.instance.author = self.request.user
        form.instance.save()

        success_url = f'/profile/{self.request.user.username}/'

        return redirect(success_url)


@method_decorator(login_required, name='dispatch')
class post_edit(UpdateView):
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = '/posts/<pk>/'

    def dispatch(self, request, *args, **kwargs):
        updated_post = self.get_object()
        if updated_post.author != self.request.user:
            return redirect(f'/posts/{updated_post.pk}/')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_context_data(self, **kwargs):
        context = super(post_edit, self).get_context_data(**kwargs)
        context['is_edit'] = True
        return context

    def form_valid(self, form):
        form.instance.save()

        success_url = f'/posts/{self.object.pk}/'

        return redirect(success_url)
