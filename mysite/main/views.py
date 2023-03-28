from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Post


# Create your views here.
class HomeView(ListView):
    model = Post
    # template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "main/components/post-list-elements.html"
        return "main/index.html"


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status="published")
    related = Post.objects.filter(author=post.author)[:5]
    return render(
        request,
        "main/single.html",
        {
            "post": post,
            "related": related,
        },
    )
