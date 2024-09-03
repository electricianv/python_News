from django.urls import path
from .views import (
    NewsListView, NewsCreateView, NewsUpdateView, NewsDeleteView,
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView,
    ArticleListView, ArticleDetailView, Posts, CategoryListView, subscribe
)
from .forms import NewsForm, ArticleForm
from django.views.decorators.cache import cache_page



urlpatterns = [
    path('', cache_page(60) (NewsListView.as_view()), name='news_list'),
    path('news/create/', cache_page(300)(NewsCreateView.as_view(form_class=NewsForm)), name='news_form'),
    path('news/<int:pk>/edit/', cache_page(300) (NewsUpdateView.as_view(form_class=NewsForm)), name='news_update_form'),
    path('news/<int:pk>/delete/', cache_page(300) (NewsDeleteView.as_view()), name='news_confirm_delete'),

    path('news/categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('',Posts.as_view(), name='posts'),
    path('news/categories/<int:pk>/subscribe/', subscribe, name='subscribe'),


    path('articles/', ArticleListView.as_view(), name='article_list'),  # Список статей
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),  # Просмотр статьи
    path('articles/create/', ArticleCreateView.as_view(form_class=ArticleForm), name='article_form'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(form_class=ArticleForm), name='article_update_form'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_confirm_delete'),
]
