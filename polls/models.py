from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


# use command       python manage.py shell          to open an interactive window and manipulate database
# Example:

# >>> from polls.models import Choice
# >>> Question.objects.all()
# >>> q = Question(question_text="What's new?", pub_date=timezone.now())
# >>> q.save()
# >>> q.id
# >>> Question.objects.all()
# >>> Question.objects.all().delete()


class Question(models.Model):
    """
    Stores question_text column, published date
    """

    question_text = models.CharField(max_length=200)
    # change TIME_ZONE in settings if the publish date is showing false value when added
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        """
        was_published_recently method should not return True if the date corresponds to future and past date
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """
    Stores single choice, related to :model:`Question`, title of choice,
    and total count of how many times this choice was selected
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Voter(models.Model):
    """
    Stores single voter, related to :model:`Choice`
    and voter's nickname
    """
    chosen_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voter_name = models.CharField(max_length=60)
    def __str__(self):
        return self.voter_name
