# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app.models import *

# Register your models here.


admin.site.register(Categories)
admin.site.register(Courses)
admin.site.register(Linkcourses)
admin.site.register(Audiobooks)
admin.site.register(Linkaudios)