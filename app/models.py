# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Categories'


class Courses(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'Courses'


class Linkcourses(models.Model):
    namelink = models.CharField(max_length=125, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='course')

    class Meta:
        managed = False
        db_table = 'Linkcourses'


class Audiobooks(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audiobooks'

    def __unicode__(self):
    	return ("%s | %s") % (self.title, self.authors)



class Linkaudios(models.Model):
    namelink = models.CharField(max_length=125, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    audiobook = models.ForeignKey(Audiobooks, models.DO_NOTHING, db_column='audiobook')

    class Meta:
        managed = False
        db_table = 'linkaudios'

    def __unicode__(self):
    	return ("%s | %s") % (self.namelink, self.url)

class Credentialskey(models.Model):
    name = models.CharField(max_length=125, blank=True, null=True)
    acronym = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credentialskey'

class Moocs(models.Model):
    title = models.CharField(max_length=245, blank=True, null=True)
    offer = models.CharField(max_length=145, blank=True, null=True)
    date = models.CharField(max_length=65, blank=True, null=True)
    link = models.CharField(max_length=45, blank=True, null=True)
    credentialskey = models.ForeignKey(Credentialskey, models.DO_NOTHING, db_column='credentialskey')

    class Meta:
        managed = False
        db_table = 'moocs'

class Movies(models.Model):
    title = models.CharField(max_length=345, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'movies'

class Languages(models.Model):
    title = models.CharField(max_length=145, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class Linklanguages(models.Model):
    namelink = models.CharField(max_length=125, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    languages = models.ForeignKey(Languages, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'linklanguages'


class Ebooks(models.Model):
    title = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebooks'


class Linkebooks(models.Model):
    namelink = models.CharField(max_length=245, blank=True, null=True)
    url = models.CharField(max_length=45, blank=True, null=True)
    ebooks = models.ForeignKey(Ebooks, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'linkebooks'


class Textbooks(models.Model):
    title = models.CharField(max_length=245, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=445, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'textbooks'