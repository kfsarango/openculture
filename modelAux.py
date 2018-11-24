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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Credentialskey(models.Model):
    name = models.CharField(max_length=125, blank=True, null=True)
    acronym = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credentialskey'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Linkaudios(models.Model):
    namelink = models.CharField(max_length=125, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    audiobook = models.ForeignKey(Audiobooks, models.DO_NOTHING, db_column='audiobook')

    class Meta:
        managed = False
        db_table = 'linkaudios'


class Moocs(models.Model):
    title = models.CharField(max_length=245, blank=True, null=True)
    offer = models.CharField(max_length=145, blank=True, null=True)
    date = models.CharField(max_length=65, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    credentialskey = models.ForeignKey(Credentialskey, models.DO_NOTHING, db_column='credentialskey')

    class Meta:
        managed = False
        db_table = 'moocs'


class Movies(models.Model):
    title = models.CharField(max_length=345, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'movies'
