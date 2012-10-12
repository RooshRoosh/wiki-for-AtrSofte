# -*- coding: utf-8 -*-
# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from pages.models import Page,Relations
from django.template.defaultfilters import slugify
from slug_processor import slugfy
import re

def index(request):
    r = [i.child for i in Relations.objects.all()]
    p = Page.objects.all()
    page_list = []
    for j in p:
        if not j in r:
            page_list.append(j)
    return render_to_response('index.html', {'page_list':page_list})

def get_page(request, page):
    p = get_object_or_404(Page, slug=page)
    p_referense = Relations.objects.filter(child=p)
    if p_referense:
        p_referense = p_referense[0] 
    child_referense = Relations.objects.filter(page=p)
    context = {'page':p,
               'p_referense':p_referense,
               'child_referense':child_referense,
               }
    return render_to_response('page.html', context)
    

def add_page(request, page='main'):
    if request.POST:
        title = request.POST['title']
        text = request.POST['text']
        if request.POST.has_key('slug'):
            if request.POST['slug']:
                slug = slugfy(request.POST['slug'])
            else:
                slug = slugfy(title)
        else:
            slug = slugfy(title)
        if Page.objects.filter(slug=slug):
            error = 'Страница с таким URL уже существует. Пожалуйста назовите материал иначе (Допишите категорию, например: "Фильм2012", Фильм1984", "Книга", "Мьюзикл", "Пресс-релиз")'
            return render_to_response('cre.html', {'error':error,
                                                   'title':title,
                                                   'text':text,
                                                   'slug':slug###########№№
                                                   }, context_instance = RequestContext(request))
        new_page = Page(title = title,
                        text = text,
                        slug=slug)
        new_page.save()
        if page == 'main':
            return redirect(new_page)
        else:
            p = get_object_or_404(Page, slug=page)
            a = Relations(child=new_page, page=p)
            a.save()
            return redirect(new_page)#redirect(new_page)
    else:
        context={}
        if request.GET.has_key('ntitle'):
            context = {'title':request.GET['ntitle']}
        return render_to_response('cre.html', context, context_instance = RequestContext(request))


def edit_page(request, page='main'):
    p = get_object_or_404(Page, slug=page)
    if request.POST:
        p.title = request.POST['title']
        p.text = request.POST['text']
        p.save()
        return redirect(p)
    else:
        return render_to_response('cre.html',
                                  {'title':p.title,
                                   'text':p.text},
                                  context_instance = RequestContext(request))        


def delete_page(request, page='main'):
    p = get_object_or_404(Page, slug=page)
    if request.POST:
        if request.POST.has_key('Yes'):
            parent = Relations.objects.filter(child=p)
            childs = Relations.objects.filter(page=p)
            #################################################################################
            ##Если не нужно поддерживать связь между родителем и внуками то этот код лишний##
            #################################################################################
            if parent:
                if childs:
                    for child in childs:
                        child.page = parent[0].page
                        child.save()
                else:
                    for child in childs:
                        child.delete()
            else:
                if childs:
                    for child in childs:
                        child.delete()
            #################################################################################
            p.delete()
            if parent:
                return redirect(parent[0].page)
            else:
                return redirect('/add/')
            
        else:
            return redirect(p)
    else:
        return render_to_response('delete.html',
                                  {'title':p.title,
                                   'text':p.text},
                                  context_instance = RequestContext(request))        

        
