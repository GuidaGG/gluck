from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

# Create your models here.
class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default="new page", max_length=300)
    
    def __str__(self):
        return self.title

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, default=None)
    section_title = models.TextField(null=False, max_length=50, default="section title")
    def __str__(self):
       return self.section_title



class Image(models.Model):
    IMAGE_SIZES = (
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    section_fk = models.ForeignKey(Section, on_delete=models.CASCADE, default=None)
    order = models.CharField(blank=True, null=True, max_length=10)
    image = models.ImageField(blank=True, null=True)
    size = models.CharField(max_length=1, choices=IMAGE_SIZES, default="M")
    image_tag = models.CharField(blank=True, null=True, max_length=10)
    def __str__(self):
        return ''
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image Preview'
    image_tag.allow_tags = True

    def return_m(self):
        return self.section_fk


class Text(models.Model):
    section_fk = models.ForeignKey(Section, on_delete=models.CASCADE, default=None)
    order = models.CharField(blank=True, null=True, max_length=10)
    text = RichTextField(blank=True, null=True)
    imaget = models.ImageField(blank=True, null=True)
    imaget_tag = models.CharField(blank=True, null=True, max_length=10)
    def __str__(self):
        return ''
    
    def imaget_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.imaget))

    imaget_tag.short_description = 'Image Preview'
    imaget_tag.allow_tags = True
 
    def return_m(self):
        return self.section_fk

class Event(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, default="true")
    date = models.DateField()
    time = models.TimeField()
    price = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    published_date = timezone.now()
    
    def is_active(self):
        if self.date  < timezone.now():
            return True
        else:
            return False  

    def __str__(self):
        return self.title

    def get_year(self):
        return self.date.year
    

