from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.order_by()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #returns the 4 newest stories
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        #returns the oldest 4 stories
        context['old_stories'] = NewsStory.objects.order_by('pub_date')[:4]
        
        return context

# Alany 26/12/2022 
# Add view for a single story
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

# add view to use Storyform 
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
