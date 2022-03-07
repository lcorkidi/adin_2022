from os import path
from django import template
from django.utils.html import format_html
from adin.settings import BASE_DIR

register = template.Library()
FILE_TMPL = path.join(BASE_DIR,'static/icons-1.7.0/icons/%s.svg')

@register.simple_tag(name='render_bi')
def render_bootstrap_icon(icon_name, icon_class: str = None, width: str = None, height: str = None):
    html = open(FILE_TMPL % icon_name,'r').read()
    if icon_class: html = html.replace('class="bi', 'class="bi '+icon_class+' ')
    for token,value in zip(('width','height'),(width,height)):
        token += '="%s"'
        if value: html = html.replace(token % "1em",token % value)
    return format_html(html)

@register.simple_tag(name="app_name")
def app_name():
    return 'AdIn'

@register.simple_tag(name="selected_choice")
def selected_choice(form, field_name, field_value):
    return dict(form.fields[field_name].choices)[field_value]