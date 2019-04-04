from django.db import models

class Topic(models.Model):
    Main_heading = models.CharField(primary_key=True, max_length=100)
    image_url = models.CharField(max_length=100,default="/images/")
    no_of_views = models.IntegerField(default=0)
    no_of_posts = models.IntegerField(default=0)
    description = models.CharField(max_length=500)

class Question(models.Model):
    question = models.CharField(max_length=500)
    q_dt = models.CharField(max_length=500)

class Answer(models.Model):
    q_id = models.IntegerField()
    q_dt = models.CharField(max_length=500)
    a_dt = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=2000)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

class AnswerFlag(models.Model):
    q_id = models.IntegerField()
    username = models.CharField(max_length=500)
    up_flag = models.BooleanField(default=False)
    down_flag = models.BooleanField(default=False)

class Comment(models.Model):
    ans_id = models.IntegerField()
    comment = models.CharField(max_length=2000)
    #dt = models.DateTimeField()
########UMAAAAAAA