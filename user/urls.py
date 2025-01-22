from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView, user_profile

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

urlpatterns += [
    path('profile/', user_profile, name='profile'),
]