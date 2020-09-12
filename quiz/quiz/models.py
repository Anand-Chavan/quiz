from django.db import models

class User(models.Model):
    user_id   =  models.IntegerField(primary_key=True)
    username  =  models.CharField(max_length=50)
    useremail =  models.CharField(max_length=300)
    userpass =  models.CharField(max_length=300)
    regtime  =  models.DateField()


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True),
    question    = models.CharField(max_length=300)
    is_active   = models.IntegerField()

class Question_choices(models.Model):
    choice_id = models.IntegerField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_right_choice = models.IntegerField(primary_key=True)
    choice = models.CharField(max_length=50)

class User_question_answer(models.Model):
    user_id      = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id  = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id    = models.ForeignKey(Question_choices, on_delete=models.CASCADE)
    is_right     = models.IntegerField(primary_key=True)
    answer_time  = models.DateField()
