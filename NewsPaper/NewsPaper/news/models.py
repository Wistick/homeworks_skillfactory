from django.db import models
from accounts.models import User


class Author(models.Model):
    """
    Модель, содержащая объекты всех авторов.
    Имеет следующие поля:
    cвязь «один к одному» с встроенной моделью пользователей User;
    рейтинг пользователя.
    """
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # TODO
        """
        Метод update_rating() модели Author, который обновляет рейтинг пользователя, переданный в аргумент этого метода.
        Он состоит из следующего:
        суммарный рейтинг каждой статьи автора умножается на 3;
        суммарный рейтинг всех комментариев автора;
        суммарный рейтинг всех комментариев к статьям автора.
        """
        rating = self.rating
        pass


class Category(models.Model):
    """
    Категории новостей / статей — темы, которые они отражают(спорт, политика, образование и т.д.).
    Имеет единственное поле: название категории.Поле должно быть уникальным(в определении поля необходимо написать
    параметр unique = True).
    """
    name = models.CharField(max_length=60, unique=True)


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

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choice_filed = models.CharField(
        max_length=2,
        choices=POST_CHOICES,
        default=news
    )
    time_created = models.DateTimeField(auto_now_add=True)
    post = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField('Напишите сюда свой текст вашей статьи')
    rating = models.IntegerField(default=0)

    def preview(self):
        """
        Метод preview() модели Post, который возвращает начало статьи
        (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
        """
        text = self.text
        pass

    def like(self):
        """
        Метод like() в моделях Comment и Post, который увеличивает рейтинг на единицу.
        """
        rating = self.rating
        pass

    def dislike(self):
        """
        Метод dislike() в моделях Comment и Post, который уменьшает рейтинг на единицу.
        """
        rating = self.rating


class PostCategory(models.Model):
    """
    Промежуточная модель для связи «многие ко многим»:
    связь «один ко многим» с моделью Post;
    связь «один ко многим» с моделью Category.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    
    def like(self):
        """
        Метод like() в моделях Comment и Post, который увеличивает рейтинг на единицу.
        """
        rating = self.rating
        pass

    def dislike(self):
        """
        Метод dislike() в моделях Comment и Post, который уменьшает рейтинг на единицу.
        """
        rating = self.rating
