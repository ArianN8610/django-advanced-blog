from django.urls import path
from django.views.generic import TemplateView, RedirectView
from . import views

app_name = 'blog'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html', extra_context={'name': 'Arian'}), name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path('go-to-index/', RedirectView.as_view(pattern_name='blog:index'), name='redirect-to-index'),
    path('go-to-index/', views.RedirectToIndex.as_view(), name='redirect-to-index'),
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
]
