from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.

# Signup View
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login')
    
# Login view
class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    
# Logout view
class CustomLogoutView(LogoutView):
    template_name = 'user/logout.html'
    
@login_required
def user_profile(request):
    user = request.user
    return render(request, 'user/profile.html', {'user': user})