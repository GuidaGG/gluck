import random
from django import template
import datetime
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def define(val=None):
  return val

@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)

@register.simple_tag
def checkeven(a):
    if (a % 2) == 0:
        return "even"
    else:
        return 'odd'
    endif
   

@register.simple_tag
def random_class():
    classes = ["twenty", "thirty", "forthy"]
    r = random.randint(0, 2)
    return classes[r]

@register.simple_tag
def random_class_images():
    classes = ["forty", "fifty", "sixty"]
    r = random.randint(0, 2)
    return classes[r]

@register.simple_tag
def random_align():
    classes = ["left", "right"]
    r = random_int(0,1)

    return classes[r]

@register.simple_tag
def is_open():
    now = datetime.datetime.now()
    now = datetime.datetime(2019, 11, 15, 14, 0)
    currentday = now.weekday()
    currenthour  = now.hour

    if((currentday!=6 or currentday!=5 or currentday!=0) and (currenthour>12 and currenthour<19) ):
        return mark_safe('<div class="opening">Gerade geöffnet</div><div class="closing">Schließt Um 19 Uhr</div>')
    else:
        return ""


