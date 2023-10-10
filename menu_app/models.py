from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Name')
    slug = models.SlugField(max_length=150)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Category')
    content = models.TextField(verbose_name='Content')

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.content

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Name')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Parent category')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title