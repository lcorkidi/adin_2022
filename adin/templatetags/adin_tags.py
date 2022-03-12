from os import path
from django import template
from django.utils.html import format_html
from adin.settings import BASE_DIR

from people.models import Person, Person_Natural, Person_Legal, Person_E_Mail, Person_Address, Person_Phone
from references.models import Address, PUC, E_Mail, Phone
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Estate_Appraisal

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
    try:
        return dict(form.fields[field_name].choices)[field_value]
    except:
        return dict(form.fields[field_name].choices)[int(field_value)]

@register.simple_tag(name='fk_str')
def fk_str(form, field_name):
    try:
        return eval(f'form.instance.{field_name}')
    except:
        try:
            return eval(f'{form._meta.model._meta.get_field(field_name).related_model.__name__}.objects.get(pk={form[field_name].value()})')
        except:
            return eval(f'{form._meta.model._meta.get_field(field_name).related_model.__name__}.objects.get(pk="{form[field_name].value()}")')
        