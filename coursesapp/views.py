from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import RegistrationForm
from .models import Course


def main_page(request):
    user = request.user
    return render(request, 'main_page.html', {'user': user})


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': RegistrationForm()
        }
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
        else:
            context = {
                'form': form
            }
        return render(request, 'registration/register.html', context)


class Courses(ListView):
    model = Course
    queryset = Course.objects.all()