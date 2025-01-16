from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post


def home_view(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'post_list': posts})


class HomePageView(ListView):
    template_name = "home.html"
    model = Post  # context = {'post_list': [post1, post1 etc]}

class HomePageTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *kwargs):
        # posts = ['hello', '2. post', 'hello again']
        posts = Post.objects.all()
        context = {
            'post_list': posts
        }
        return context

