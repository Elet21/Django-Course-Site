from django.urls import path, include
from .views import main_page, Register, Courses

urlpatterns = [
    path('', main_page, name='main_page'),
    path('register/', Register.as_view(), name='register'),
    path('courses/', Courses.as_view(), name='courses')
]