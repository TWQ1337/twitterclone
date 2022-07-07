from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'authoperations/login.html'
    extra_context = {
        'page': 'login'
    }


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('fp')
        else:
            return redirect('fp')
    else:
        form = UserCreationForm()
        context = {
            'page': 'register',
            'form': form
        }
        return render(request, 'authoperations/login.html', context)


