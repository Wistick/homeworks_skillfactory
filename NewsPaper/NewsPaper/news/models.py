from django.db import models
from django.conf import settings


class Author(models.Model):
    """
    Модель, содержащая объекты всех авторов.
    Имеет следующие поля:
    cвязь «один к одному» с встроенной моделью пользователей User;
    рейтинг пользователя.
    """
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

        posts_author = Post.objects.filter(post_author=self.author_user)
        post_rating = sum([r.post_rating for r in posts_author])
        print(post_rating)
        comment_rating = sum([r.comment_rating for r in Comment.objects.filter(comment_author=self.author_user)])
        print(comment_rating)

        likes_author_comment_sum = sum([r.comment_rating for r in Comment.objects.filter(comment_post__in=posts_author)])
        print(likes_author_comment_sum)
        self.rating = post_rating + comment_rating + likes_author_comment_sum
        print(self.rating)
        self.save()

    def __str__(self):
        return f'{self.author_user}'


class Category(models.Model):
    """
    Категории новостей / статей — темы, которые они отражают(спорт, политика, образование и т.д.).
    Имеет единственное поле: название категории.Поле должно быть уникальным(в определении поля необходимо написать
    параметр unique = True).
    """
    category_name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Post(models.Model):
    """
    Эта модель должна содержать в себе статьи и новости, которые создают пользователи.
    Каждый объект может иметь одну или несколько категорий.
    Соответственно, модель должна включать следующие поля:
    связь «один ко многим» с моделью Author;
    поле с выбором — «статья» или «новость»;
    автоматически добавляемая дата и время создания;
    связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
    заголовок статьи/новости;
    текст статьи/новости;
    рейтинг статьи/новости.
    """
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
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')  # default=timezone.now
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField('Напишите сюда свой текст вашей статьи')
    post_rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def preview(self):
        """
        Метод preview() модели Post, который возвращает начало статьи
        (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
        """
        return self.text[:125] + '...'

    def like(self):
        """
        Метод like() в моделях Comment и Post, который увеличивает рейтинг на единицу.
        """
        self.post_rating += 1
        self.save()

    def dislike(self):
        """
        Метод dislike() в моделях Comment и Post, который уменьшает рейтинг на единицу.
        """
        self.post_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.post_author}'


class PostCategory(models.Model):
    """
    Промежуточная модель для связи «многие ко многим»:
    связь «один ко многим» с моделью Post;
    связь «один ко многим» с моделью Category.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} - {self.post}'


class Comment(models.Model):
    """
    Под каждой новостью/статьей можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
    Модель будет иметь следующие поля:
    связь «один ко многим» с моделью Post;
    связь «один ко многим» с встроенной моделью User
    (комментарии может оставить любой пользователь, не обязательно автор);
    текст комментария;
    дата и время создания комментария;
    рейтинг комментария.
    """
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    time_created = models.DateTimeField(auto_now_add=True)  # default=timezone.now
    comment_rating = models.IntegerField(default=0)

    def like(self):
        """
        Метод like() в моделях Comment и Post, который увеличивает рейтинг на единицу.
        """
        self.comment_rating += 1
        self.save()

    def dislike(self):
        """
        Метод dislike() в моделях Comment и Post, который уменьшает рейтинг на единицу.
        """
        self.comment_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.comment_author}'
