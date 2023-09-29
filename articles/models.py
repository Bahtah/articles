from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey

from django.db import models


class Category(MPTTModel):
    title = models.CharField('Заголовок', max_length=255)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])


class Article(models.Model):
    category = TreeForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    title = models.CharField("Статьи", max_length=255)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="articles/images")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"