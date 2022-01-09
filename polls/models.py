
import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def get_absolute_url(self):
        return reverse(args=[str(self.id)]) # noqa F821

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class ModelLog(models.Model):
    path = models.CharField(max_length=300)
    method = models.CharField(max_length=30)
    timestamp = models.TimeField(auto_now=True)

    def __str__(self):
        return self.path
