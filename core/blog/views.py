from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView, CreateView, UpdateView, \
    DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import PostCreateForm
from .models import Post


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Arian'
        return context


class RedirectToIndex(RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'blog:index'


class PostListView(PermissionRequiredMixin, ListView):
    permission_required = 'blog.view_post'
    # model = Post
    queryset = Post.published.all()
    template_name = 'blog/posts.html'  # Default -> blog/post_list.html
    context_object_name = 'posts'  # Default -> object_list
    paginate_by = 2
    ordering = '-id'

    # def get_queryset(self):
    #     posts = Post.published.all()
    #     return posts


class PostDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'blog.view_post'
    queryset = Post.published.all()
    context_object_name = 'post'


# class PostCreateView(FormView):
#     template_name = 'blog/create.html'
#     form_class = PostCreateForm
#     success_url = '/blog/post/'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.create_post'
    # fields = '__all__'
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/create.html'

    # success_url = '/blog/post/'  # Default -> current post url -> blog/post/5

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.change_post'
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/create.html'


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'blog.delete_post'
    model = Post
    template_name = 'blog/delete.html'
    success_url = '/blog/post/'
