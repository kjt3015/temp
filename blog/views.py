# blog/views
# from django.shortcuts import render

from .models import Post

#CBV 방식으로 페이지 작성
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/posts.html'

    
class PostDetail(DetailView):
    model = Post

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
    
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
    
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )