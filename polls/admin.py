# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  # fields = ['pub_date', 'question_text']
  fieldsets = [
    (None,               {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date']}),
  ]
  inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

# Register your models here.
