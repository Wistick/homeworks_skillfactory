from django.db import models
from django.conf import settings


class Author(models.Model):
    author_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        """
        Метод update_rating() модели Author, который обновляет рейтинг пользователя, переданный в аргумент этого метода.
        Он состоит из следующего:
        суммарный рейтинг каждой статьи автора умножается на 3;
        суммарный рейтинг всех комментариев автора;
        суммарный рейтинг всех комментариев к статьям автора.
        """
        sum_post = 0
        post = Post.objects.filter(post_author=self).values('post_rating')
        for i in post:
            sum_post = sum_post + i.get('post_rating') * 3

        sum_comment = 0
        comment = Comment.objects.filter(comment_author=self.author_user).values('comment_rating')
        for i in comment:
            sum_comment = sum_comment + i.get('comment_rating')

        sum_post_comment = 0
        post_comment = Comment.objects.filter(comment_post__post_author=self).values('comment_rating')
        for i in post_comment:
            sum_post_comment = sum_post_comment + i.get('comment_rating')

        self.author_rating = sum_post + sum_comment + sum_post_comment
        self.save()

    def __str__(self):
        return f'{self.author_user}'


class Category(models.Model):
    category_name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Post(models.Model):
    article = 'AR'
    news = 'NE'

    POST_CHOICES = (
        (article, 'Статья'),
        (news, 'Новость'),
    )

    post_author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    choice_field = models.CharField(
        max_length=2,
        choices=POST_CHOICES,
        default=news
    )
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField('Напишите сюда свой текст вашей статьи')
    post_rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def preview(self):
        return self.text[:125] + '...'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.post_author} - {self.title} - {self.text} - {self.post_category.all()}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} - {self.post}'


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    time_created = models.DateTimeField(auto_now_add=True)  # default=timezone.now
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.comment_author}'
