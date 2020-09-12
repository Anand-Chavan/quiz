from django.contrib import admin

# Register your models here.

from .models import User,Question,Question_choices,User_question_answer

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Question_choices)
admin.site.register(User_question_answer)