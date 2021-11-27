from django.db import models
from django.urls import reverse
from datetime import date

TOPICS = (
    ('R', "Real Life"),
    ('H', "Haunting"),
    ('N', "Nightmare")
)


class Forum(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  comment = models.TextField(max_length=250)
  spookyLevel = models.IntegerField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('forums_detail', kwargs={'Forum_id': self.id})


class Posts(models.Model):
  date = models.DateField("Post date")
  topic = models.CharField(
      max_length=1,
      choices=TOPICS,
      default=TOPICS[0][0]
  )
  forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

  class Meta:
    ordering = ['-date']

  def __str__(self):
    return f"{self.get_topic_display()} on {self.date}"

  def posts_for_today(self):
    return self.posts_set.filter(date=date.today()).count() >= len(TOPICS)
