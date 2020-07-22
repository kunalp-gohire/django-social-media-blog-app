from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import Http404,HttpResponseRedirect
from braces.views import SelectRelatedMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.




class PostList(SelectRelatedMixin,generic.ListView):
    model = models.Post
    select_related = ('user',)


class UserPosts(generic.ListView):
    model= models.Post
    template_name = 'post/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    
    model = models.Post   
    form_class = forms.PostForm
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form) 


class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user',)
    success_url = reverse_lazy('posts:all')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(request, *args, **kwargs)



    
    
        





############
#function based
###########



@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(models.Post,pk=pk)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        form = forms.CommentForm()
    return render(request,'post/comment_form.html',{'form':form})



@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(models.Comment,pk=pk)
    post_pk = comment.post.pk 
    comment.delete()
    return redirect(comment.post.get_absolute_url())



 
    

