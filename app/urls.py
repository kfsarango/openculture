# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^scrapy/courses[/]+$', views.scrapy_courses, name='scrapy_courses'),
    url(r'^scrapy/audio/books[/]+$', views.scrapy_audio_books, name='scrapy_audio_books'),
    url(r'^scrapy/moocs[/]+$', views.scrapy_moocs, name='scrapy_moocs'),
    url(r'^scrapy/movies[/]+$', views.scrapy_movies, name='scrapy_movies'),
    url(r'^scrapy/languajes[/]+$', views.scrapy_languajes, name='scrapy_languajes'),
    url(r'^scrapy/text_books[/]+$', views.scrapy_textbooks, name='scrapy_textbooks'),
    url(r'^scrapy/e_books[/]+$', views.scrapy_ebooks, name='scrapy_ebooks'),
    
]