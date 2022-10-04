from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import RecipeForm


@login_required
def add_post(request):
    """
    View to add recipe.
    """
    print(request.user)
    post_form = PostForm(request.POST, request.FILES)

    if request.method == 'POST':
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.title = post_form.title
            post_form.author = request.user
            post_form.status = 1
            post_form.save()
            return redirect(reverse('blog/posts.html'))

    context = {
        'post_form': post_form
    }

    return render(request, 'add_post.html', context)


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/posts.html'
    paginate_by = 6


class PostDetail(View):
    """
    Recipe detail view to display full recipe when clicked on.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )