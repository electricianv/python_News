from django.urls import path
from .views import (
    NewsListView, NewsCreateView, NewsUpdateView, NewsDeleteView,
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView,
    ArticleListView, ArticleDetailView, Posts, CategoryListView, subscribe
)
from .forms import NewsForm, ArticleForm
from .views import IndexView



urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('news/create/', NewsCreateView.as_view(form_class=NewsForm), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(form_class=NewsForm), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),

    path('news/categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('',Posts.as_view(), name='posts'),
    path('news/categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('', IndexView.as_view()),

]
