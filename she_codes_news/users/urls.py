from django.contrib.auth import views as auth_views
from django.urls import path
from .views import CreateAccountView, EditAccountView, ProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/view-profile', ProfileView.as_view(), name='viewAccount' ),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('<int:pk>/update-account/', EditAccountView.as_view(), name='updateAccount'),
]