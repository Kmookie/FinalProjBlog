from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import Post
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return Post.objects.order_by('-timestamp')
        
class DeleteView(generic.DeleteView):
    model = Post
    template_name = 'detail.html'
    
    def get_success_url(self):
        return '/'

    # def delete(request, pk):
    #     Post.objects.get(pk=pk).delete()
    #     # return HttpResponseRedirect('/')
    

def add_post(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return HttpResponseRedirect('/')
    

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
