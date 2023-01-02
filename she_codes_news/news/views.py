# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import NewsStory
from .forms import StoryForm, CommentForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #returns the 4 newest stories
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date', '-id')[:4]
        #returns the oldest 4 stories
        context['old_stories'] = NewsStory.objects.all().order_by('pub_date')[:4]

        
        return context

# Alany 26/12/2022 
# Add view for a single story
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["form_action"] = reverse_lazy('news:addComment', kwargs={'pk':self.kwargs.get('pk')})
        return context

class ListStoriesView(generic.ListView):
    template_name = 'news/allStories.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # #returns all stories
        context['list_stories'] = NewsStory.objects.all().order_by('-pub_date')
        
        return context
# add view to use Storyform 

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'redirect_to'

    form_class = CommentForm
    template_name = "news/createComment.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form)

    def get_success_url(self) -> str:
        pk = self.kwargs.get("pk")
        return reverse_lazy('news:story', kwargs={'pk':pk})
