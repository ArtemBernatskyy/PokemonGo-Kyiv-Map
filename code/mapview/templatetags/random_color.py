from django import template
import random


register = template.Library()


@register.simple_tag
def random_color():
    r = lambda: random.randint(0,255)
    color_data = '%02X%02X%02X' % (r(),r(),r())
    return color_data