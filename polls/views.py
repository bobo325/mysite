from django.db.models import F
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from polls.models import Question, Choice


# def index(request):
#     # 注意这里，排序参数前如果有‘-’则代表着降序，没有则默认升序
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]  # alt+回车(导包快捷键)
#
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     # response = "You're looking at the question of question %s."
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist!")
#     return render(request, 'polls/detail.html', {'question': question})
#     # return HttpResponse(response % question_id)
#
#     # 或者有一个快捷函数
#     # question = get_object_or_404(Question, pk=question_id)
#     # 还有一个get_list_or_404()  函数
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])  # request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID。
#     except(KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             "question": question,
#             "error_message": "You didn't select a choice."
#         })
#     else:
#         # description  6部分
#         # selected_choice.votes += 1
#         selected_choice.votes = F('votes') + 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# ListView (DetailView)使用一个叫做 <app name>/<model name>_list.html 的默认模板；
# 我们使用 template_name 来告诉 ListView 使用我们创建的已经存在的 "polls/index.html" 模板。
class IndexView(generic.ListView):
    # model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):  # This is a model instance looked up from `self.queryset`
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID。
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        # description  6部分
        # selected_choice.votes += 1
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
