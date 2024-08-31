from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Post, Category
from django.utils import timezone


@shared_task
def hello():
    print("Hello, world!")


@shared_task
def send_news_notification(post_id):
    post = Post.objects.get(id=post_id)
    subscribers = post.category.subscribers.all()

    for user in subscribers:
        send_mail(
            subject=f"New post in {post.category.name}",
            message=post.text,
            from_email=settings.DEFAULT_FROM_EMAIL,  # Используем email из настроек
            recipient_list=[user.email],
        )


@shared_task
def send_weekly_news():
    last_week = timezone.now() - timezone.timedelta(days=7)
    last_week_posts = Post.objects.filter(created_at__gte=last_week)

    categories = Category.objects.all()
    for category in categories:
        subscribers = category.subscribers.all()
        post_titles = "\n".join([post.title for post in last_week_posts if post.category == category])
        for user in subscribers:
            send_mail(
                subject=f"Weekly Digest for {category.name}",
                message=f"Here are the new posts in your subscribed category:\n\n{post_titles}",
                from_email=settings.DEFAULT_FROM_EMAIL,  # Используем email из настроек
                recipient_list=[user.email],
            )
