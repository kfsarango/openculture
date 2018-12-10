# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class NativeDowloads(models.Model):
    low = models.TextField(blank=True, null=True)
    medium = models.TextField(blank=True, null=True)
    high = models.TextField(blank=True, null=True)
    audiodownload = models.TextField(blank=True, null=True)
    talks = models.ForeignKey('Talks', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'native_dowloads'


class Ratings(models.Model):
    name = models.CharField(max_length=145, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'


class RelatedTalks(models.Model):
    talk_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=245, blank=True, null=True)
    speaker = models.CharField(max_length=245, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=345, blank=True, null=True)
    talks = models.ForeignKey('Talks', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'related_talks'


class Speakers(models.Model):
    speaker_id = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=245, blank=True, null=True)
    is_published = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=85, blank=True, null=True)
    lastname = models.CharField(max_length=85, blank=True, null=True)
    middleinitial = models.CharField(max_length=245, blank=True, null=True)
    title = models.CharField(max_length=245, blank=True, null=True)
    description = models.CharField(max_length=245, blank=True, null=True)
    photo_url = models.TextField(blank=True, null=True)
    whatotherssay = models.TextField(blank=True, null=True)
    whotheyare = models.TextField(blank=True, null=True)
    whylisten = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speakers'


class SubtitledDownloads(models.Model):
    name = models.CharField(max_length=145, blank=True, null=True)
    low = models.TextField(blank=True, null=True)
    high = models.TextField(blank=True, null=True)
    talks = models.ForeignKey('Talks', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'subtitled_downloads'


class Tags(models.Model):
    name = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class TalkLanguages(models.Model):
    languagename = models.CharField(db_column='languageName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    endonym = models.CharField(max_length=45, blank=True, null=True)
    languagecode = models.CharField(db_column='languageCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ianacode = models.CharField(db_column='ianaCode', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'talk_languages'


class Talks(models.Model):
    talk_id = models.IntegerField(blank=True, null=True)
    threadid = models.CharField(max_length=45, blank=True, null=True)
    num_comments = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=345, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    event = models.CharField(max_length=245, blank=True, null=True)
    language = models.CharField(max_length=45, blank=True, null=True)
    slug = models.CharField(max_length=455, blank=True, null=True)
    institute_partner_name = models.CharField(max_length=125, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    salon_partner_name = models.CharField(max_length=45, blank=True, null=True)
    event_badge = models.CharField(max_length=45, blank=True, null=True)
    is_featured = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=345, blank=True, null=True)
    hero = models.TextField(blank=True, null=True)
    hero_load = models.TextField(blank=True, null=True)
    recorded_at = models.DateTimeField(blank=True, null=True)
    video_type = models.CharField(max_length=145, blank=True, null=True)
    viewed_count = models.CharField(max_length=45, blank=True, null=True)
    curator_approved = models.IntegerField(blank=True, null=True)
    url_talk = models.TextField(blank=True, null=True)
    row_inserted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talks'

class TalksHasSpeakers(models.Model):
    talks = models.ForeignKey(Talks, models.DO_NOTHING)
    speakers = models.ForeignKey(Speakers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'talks_has_speakers'
        unique_together = (('talks', 'speakers'),)

class TalksHasLanguages(models.Model):
    talks = models.ForeignKey(Talks, models.DO_NOTHING)
    languages = models.ForeignKey(TalkLanguages, models.DO_NOTHING)
    isrtl = models.IntegerField(db_column='isRtl', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'talks_has_languages'
        unique_together = (('talks', 'languages'),)


class TalksHasRatings(models.Model):
    talks = models.ForeignKey(Talks, models.DO_NOTHING)
    ratings = models.ForeignKey(Ratings, models.DO_NOTHING)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talks_has_ratings'
        unique_together = (('talks', 'ratings'),)


class TalksHasTags(models.Model):
    talks = models.ForeignKey(Talks, models.DO_NOTHING)
    tags = models.ForeignKey(Tags, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'talks_has_tags'
        unique_together = (('talks', 'tags'),)