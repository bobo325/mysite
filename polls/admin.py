from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('question_text',)  # 用于搜索筛选 ，使用like来模糊查询数据
    list_display = ('id', 'question_text', 'pub_date', 'was_published_recently')  # 在查看、修改的时候显示的属性
    list_display_links = ('question_text',)  # 添加<a>标签的字段
    list_filter = ('pub_date',)  # 激活过滤器
    list_per_page = 10  # 每页显示的对象数量，默认100
# class ChoiceInline(admin.TabularInline):  # 还可以填 admin.StackedInline Block显示，但不简约or节省界面空间
#     model = Choice
#     extra = 3
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
#     ]
#     inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'votes')
    list_display_links = ('choice_text',)
    list_filter = ('question',)


# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)


# Example
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     # 这个的作用是给出一个筛选机制，一般按照时间比较好
#     date_hierarchy = 'create_date'
#
#     exclude = ('views',)
#
#     # 在查看修改的时候显示的属性，第一个字段带有<a>标签，所以最好放标题
#     list_display = ('id', 'title', 'author', 'create_date', 'update_date')
#
#     # 设置需要添加<a>标签的字段
#     list_display_links = ('title',)
#
#     # 激活过滤器，这个很有用
#     list_filter = ('create_date', 'category')
#
#     list_per_page = 50  # 控制每页显示的对象数量，默认是100
#
#     filter_horizontal = ('tags', 'keywords')  # 给多选增加一个左右添加的框
#
#     # 限制用户权限，只能看到自己编辑的文章
#     def get_queryset(self, request):
#         qs = super(ArticleAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(author=request.user)
