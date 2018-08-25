import datetime

from django.db import models

# Create your models here.
from django.db.models import CharField, DateTimeField, ForeignKey, IntegerField, AutoField
from django.utils import timezone


class Question(models.Model):
    id = AutoField(primary_key=True)  # 自增字段，指定主键
    question_text = CharField(max_length=255)
    pub_date = DateTimeField('date published')
    # 给模型增加 __str__() 方法是很重要的，
    # 这不仅仅能给你在命令行里使用带来方便，
    # Django 自动生成的 admin 里也使用这个方法来表示对象。

    class Meta:
        db_table = 'question'

    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # was_published_recently.admin_order_field = 'pub_date'         # 根据那个属性判断
    was_published_recently.boolean = True          # 将True/False改为小图标
    # was_published_recently.short_description = 'Published recently?'     # 设置column名字


class Choice(models.Model):
    id = AutoField(primary_key=True)   # 自增字段，指定主键
    question = ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = CharField(max_length=255)
    votes = IntegerField(default=0)

    class Meta:
        db_table = 'choice'

    def __str__(self):
        return self.choice_text
# 迁移是 Django 对于模型定义（也就是你的数据库结构）的变
# 化的储存形式 - 没那么玄乎，它们其实也只是一些你磁盘上的文件

# 观察下面的筛选形式（!）。
# 见description   1部分
