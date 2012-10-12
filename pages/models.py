from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()

    slug = models.SlugField(max_length=200)

    def __unicode__(self):
        return '%s %s %s' %  (self.title, self.text,self.slug)

        
    def get_absolute_url(self):
        return r'/%s/' %self.slug

##    def save(self, *args, **kwargs):
##
##        super(Page, self).save(*args, **kwargs)

class Relations(models.Model):
    child = models.ForeignKey('Page')
    page = models.ForeignKey('Page', related_name='parent')
    
    def __unicode__(self):
        return '%s' % self.page.title
