from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class Person(models.Model):
    name = models.CharField('Nome', max_length=40)
    slug = models.SlugField('Slug', max_length=80)
    email = models.CharField('Email Address', max_length=100)
    title = models.CharField('Titulo', max_length=100)
    image = models.CharField('Imagem', max_length=200)
    responsibilities = models.CharField(max_length=1000, default='')
    bio = models.CharField(max_length=1000, default='')
    twitter = models.CharField(max_length=40, blank=True)
    github = models.CharField(max_length=40, blank=True)
    birthday = models.DateField(default=timezone.now)

    def get_year(self):
        return self.birthday.year

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
