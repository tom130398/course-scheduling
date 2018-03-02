# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    credit = models.IntegerField()
    curriculumid = models.ForeignKey('Curriculum', models.DO_NOTHING, db_column='curriculumid')

    class Meta:
        managed = False
        db_table = 'course'


class Curriculum(models.Model):
    groupid = models.ForeignKey('Groupstudy', models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'curriculum'


class Groupstudy(models.Model):
    code = models.CharField(max_length=255)
    degreeprogram = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'groupstudy'


class Implementation(models.Model):
    group = models.CharField(max_length=255)
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')

    class Meta:
        managed = False
        db_table = 'implementation'


class Room(models.Model):
    room = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')

    class Meta:
        managed = False
        db_table = 'room'


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'teacher'


class TeacherImplementation(models.Model):
    teacherid = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='teacherid', primary_key=True)
    implementationid = models.ForeignKey(Implementation, models.DO_NOTHING, db_column='implementationid')

    class Meta:
        managed = False
        db_table = 'teacher_implementation'
        unique_together = (('teacherid', 'implementationid'),)
