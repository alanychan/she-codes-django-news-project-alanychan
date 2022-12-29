"""
Alany 03/12/2022
- add view for a single story
04/12/2022
- add form to add newStory
- add staticfiles library
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/comment/', views.AddCommentView.as_view(), name ="addComment"),
] + staticfiles_urlpatterns()
