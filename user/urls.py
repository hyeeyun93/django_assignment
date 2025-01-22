from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView, user_profile
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
]