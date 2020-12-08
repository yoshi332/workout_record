from django.shortcuts import render,redirect
from .models import Article,Comment
from django.views import generic
from .forms import ArticleCreateForm,CommentCreateForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import Http404,JsonResponse
# Create your views here.
class ArticleListView(generic.ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 5

    def get_queryset(self):
        articles = Article.objects.all().order_by('-created_at')
        return articles

def detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")

    context = {
        'article': article,
        'comments':article.comments.order_by('-created_at')
    }
    return render(request, 'article_detail.html', context)

class ArticleCreateView(LoginRequiredMixin,generic.CreateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleCreateForm

    success_url = reverse_lazy('article:article_list')

    def form_valid(self,form):
        article = form.save(commit=False)
        article.user = self.request.user
        article.save()
        
        return super().form_valid(form)

    def form_invalid(self,form):
      
        return super().form_invalid(form)


class ArticleUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'article_update.html'
    def get_success_url(self):
        return reverse_lazy('article:article_detail',kwargs={'pk':self.kwargs['pk']})

    def form_valid(self,form):
        messages.success(self.request,'更新を完了しました')
        
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'更新ができませんでした')
        return super().form_invalid(form)


class ArticleDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article:article_list')

    def delete(self,request,*args,**kwargs):
        messages.success=(self.request,"削除しました")
        return super().delete(request,*args,**kwargs)

class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'comment_create.html'
    

    def get_success_url(self):
        return reverse_lazy('article:article_detail',kwargs={'pk':self.kwargs['num']})

   
    def form_valid(self,form):
        comment = form.save(commit=False)
        comment.article = Article.objects.get(pk=self.kwargs.get('num'))
        comment.save()
        
        return super().form_valid(form)

    def form_invalid(self,form):
        
        return super().form_invalid(form)
