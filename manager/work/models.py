from urllib.parse import MAX_CACHE_SIZE
from django.db import models



class Comment(models.Model):
    username = models.CharField(verbose_name='Имя пользователяц:', max_length=100)
    Email = models.EmailField()
    text = models.TextField()


    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['-username']

    def __str__(self):
        return self.username


    
class Category(models.Model):
    """ Category """

    name = models.CharField(verbose_name='Назвние категории:', max_length=100)
    slug = models.SlugField(max_length=255, unique=True)



    def __str__(self):
        return self.name


class Tato(models.Model):
    """ Product """

    user = models.CharField(verbose_name='Имя клиента:', max_length=100)
    title = models.CharField(max_length=200, verbose_name='Наименование')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение:', upload_to = 'image/%Y/%m/%d')
    likes = models.IntegerField(verbose_name='Лайки:', default=0)
    views = models.PositiveIntegerField(verbose_name='Просмтры:', default=0)
    description = models.TextField(verbose_name='Описание:', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена:')
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Тату'
        verbose_name_plural = 'Татуировки'


class TatoMaster(models.Model):
    """ Master Tattoo """

    name = models.CharField(verbose_name='Имя мастера:', max_length=100)
    skill = models.CharField(max_length=500, verbose_name='Стаж работы:')
    image = models.ImageField(verbose_name='Фото мастера:', upload_to = 'image/%Y/%m/%d', blank=True)
    about_us = models.TextField(verbose_name='О себе:')
    tatos = models.ForeignKey(Tato, on_delete=models.CASCADE)




    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    