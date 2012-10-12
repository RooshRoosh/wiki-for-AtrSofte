# -*- coding: utf-8 -*-
import re
from django.utils.safestring import mark_safe
from django import template
from pages.models import *
from pages.slug_processor import slugfy
register = template.Library()

@register.filter
def wiki_markup(string):
    linklist = [i.slug for i in Page.objects.all()]
    def validate_out_link(matchobj):
        s = matchobj.group('url')
        s = re.sub(r'https://','http://',s)
        if not re.match(r'http://',s):
            s = 'http://'+s
        return '<a href="%s" class="blue">\ %s</a> ' % (s,matchobj.group('text'))
    
    def validate_link(matchobj, linklist=linklist):
        page = slugfy(matchobj.group('page'))
        text = matchobj.group('text')
        if  page in linklist:
            return '<a href="/%s" class="blue"> %s</a>' %(page, text)
        else:
            return '<a href="add?ntitle=%s" class="red"> %s</a>' %(page,text)#
        
    string = re.sub(r'&quot;(.*?)&quot;', r'&laquo;\1&raquo; ',string)  #« »  
    string = re.sub(r'\[\[\b(?P<url>(https?://)?([0-9a-z\.-]+)\.([a-z]{2,6})([/\w\.-]*))\b(?P<text>.*?)\]\]',
                    #r'<a href="\g<url>">\g<text></a>', #
                    validate_out_link,
                    string)
    string = re.sub(r'\[(?P<page>\/\w+\b)(?P<text>.*?)\]\]',
                    #r'<a href="\g<page>">\g<text></a>',
                    validate_link,
                    string)
    string = re.sub(r'\*\*(.*?)\*\*',
                    r'<strong>\1</strong>',
                    string)
    string = re.sub(r'(?<!http:)(\/\/)(.*?)(?<!http:)(\/\/)',
                    r'<em>\2</em>',
                    string)
    string = re.sub(r'__(.*?)__',
                    r'<ins>\1</ins>',
                    string)
    return mark_safe(string)
##    
print wiki_markup(r'__//**[[http://yandex.ru text]]**//____ __[/page1 Page2]]___[[http://yandex.ru text]]')
