from django.test import TestCase

# Create your tests here.
# Получите или создайте автора (замените 'your_username' на реальное имя пользователя)
# author = Author.objects.get_or_create(user=User.objects.get(username='user'))

# from django.contrib.auth.models import User
# from news.models import Post, Author
#
# # Get or create the author (replace 'your_username' with the actual username)
# author, _ = Author.objects.get_or_create(user=User.objects.get(username='user'))
#
# # Create the article
# Post.objects.create(
#     author=author,  # Assign only the Author instance
#     category_type=Post.ARTICLE,
#     title='Пример статьи',
#     text='Это текст вашей статьи. Добавьте сюда больше информации.',
#     type='article'
# )
#
# # Create the news item
# Post.objects.create(
#     author=author,  # Assign only the Author instance
#     category_type=Post.NEWS,
#     title='Пример новости',
#     text='Это текст вашей новости. Добавьте сюда актуальную информацию.',
#     type='news'
# )