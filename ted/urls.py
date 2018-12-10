# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^scrapy/ted/detail[/]+$', views.scrapy_ted_detail, name='scrapy_ted_detail'),
    url(r'^scrapy/ted[/]+$', views.scrapy_ted_taks, name='scrapy_ted_taks'),
    
]