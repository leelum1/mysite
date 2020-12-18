from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Post, BlogImage
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog_app/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(is_private=False).order_by('-date_updated')
        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super(PostDetailView, self).get_context_data(**kwargs)
        ctx['images'] = BlogImage.objects.filter(blog=self.get_object()).filter(is_main=False)
        ctx['posts'] = Post.objects.all().exclude(id=self.get_object().id).order_by('date_updated')[:5][::-1]
        return ctx

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_app/blog_form.html'

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_app/blog_form.html'

    def get_context_data(self, **kwargs):
        ctx = super(PostUpdateView, self).get_context_data(**kwargs)
        ctx['images'] = BlogImage.objects.filter(blog=self.get_object())
        return ctx

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/blog_delete.html'
    success_url = reverse_lazy('blog_app:list')
