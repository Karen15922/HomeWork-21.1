from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Post
from pytils.translit import slugify 

def view_all(request):
    posts = Post.objects.all()
    context = {
            'object_list': posts,
            'title': 'все посты'
            }
    
    return render(request, 'blog/view_all.html', context)

class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return(reverse('blog:view', args=[self.kwargs.get('pk')]))

class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset

class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')



def published_toggle(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    if post.is_published:
        post.is_published = False
    else:
        post.is_published = True

    post.save()
    return redirect(reverse('blog:view_all'))