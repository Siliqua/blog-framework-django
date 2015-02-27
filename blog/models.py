from django.db import models
from django.db.models import permalink



# Create your models here.

class Blog(models.Model):
    class Meta:
            ordering = ('-posted',)
    titulo = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField()
    categoria = models.ForeignKey('blog.Categoria')
    resumo = models.TextField()

    def __unicode__(self):
        return '%s' % self.titulo

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    #def get_titulo(self):
     #   return self.titulo

class Categoria(models.Model):
    titulo = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.titulo

    @permalink
    def get_absolute_url(self):
        return ('view_blog_categoria', None, { 'slug': self.slug })

