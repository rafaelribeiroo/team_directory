from django.db import models
from django.template.defaultfilters import slugify


class Person(models.Model):
    name = models.CharField('Nome', max_length=40)
    email = models.CharField('Email Address', max_length=100)
    title = models.CharField('Titulo', max_length=100)
    slug = models.SlugField('Slug', max_length=80)
    image = models.CharField('Imagem', max_length=200)

    def save(self, *args, **kwargs):
        if not self.pk:
            slug = slugify(self.name)
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name', ]
        verbose_name = 'Person'
        verbose_name_plural = 'Peoples'
