from django.urls import path
from .views import (
    NewsListView, NewsCreateView, NewsUpdateView, NewsDeleteView,
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView,
    ArticleListView, ArticleDetailView, Posts, CategoryListView, subscribe
)
from .forms import NewsForm, ArticleForm



urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('news/create/', NewsCreateView.as_view(form_class=NewsForm), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(form_class=NewsForm), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),

    # Пути для статей
    # path('articles/', ArticleListView.as_view(), name='article_list'),  # Список статей
    # path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),  # Просмотр статьи
    # path('articles/create/', ArticleCreateView.as_view(form_class=ArticleForm), name='article_create'),
    # path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(form_class=ArticleForm), name='article_update'),
    # path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),

    path('news/categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('',Posts.as_view(), name='posts'),
    path('news/categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
]
