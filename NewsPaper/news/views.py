from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .mixins import AuthorRequiredMixin, OwnerRequiredMixin
from .models import Post, Category
from .forms import NewsForm, ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from django import forms


def no_permission(request, exception):
    return render(request, '403.html', status=403)


# def news_list(request):
#     news = Post.objects.filter(category_type=Post.NEWS)
#     paginator = Paginator(news, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'news_list.html', {'news_list': page_obj})

class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return Post.objects.filter(category_type=Post.NEWS)


class NewsCreateView(LoginRequiredMixin, AuthorRequiredMixin, CreateView):
    model = Post
    form_class = NewsForm
    template_name = 'news/news_form.html'


class NewsUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Post
    form_class = NewsForm
    template_name = 'news/news_update_form.html'


class NewsDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Post
    template_name = 'news/news_confirm_delete.html'
    success_url = '/news/'


class PostFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='Заголовок')  # Фильтр по заголовку (без учета регистра)
    category = ModelChoiceFilter(queryset=Category.objects.all(), label='Категория')  # Фильтр по категории

    class Meta:
        model = Post
        fields = ['title', 'category']


class Posts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context


class PostDeleteView(DeleteView):
    template_name = 'news/news_confirm_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category_type']


class PostUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    template_name = 'news/news_form.html'
    form_class = PostForm


# @login_required
# def upgrade_me(request):
#     user = request.user
#     premium_group = Group.objects.get(name='authors')
#     if not request.user.groups.filter(name='author').exists():
#         premium_group.user_set.add(user)
#     return redirect('/news')


class CategoryListView(Posts):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(post_category=self.category).order_by('-added_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    category = get_object_or_404(Category, id=pk)
    messages = 'You have successfully subscribed!'
    return render(request, 'news/subscribe.html', {'category': category, 'message': messages})


class ArticleUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Post
    form_class = ArticleForm
    template_name = 'articles/article_update_form.html'


class ArticleDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Post
    template_name = 'articles/article_confirm_delete.html'
    success_url = '/articles/'


class ArticleListView(ListView):
    model = Post
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(category_type=Post.ARTICLE)


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, AuthorRequiredMixin, CreateView):
    model = Post
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
