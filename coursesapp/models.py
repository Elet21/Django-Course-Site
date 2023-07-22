from django.db import models
from django.contrib.auth.models import AbstractUser


class Course(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name="Название курса")
    description = models.TextField(blank=True, verbose_name="Описание курса")
    author = models.CharField(max_length=150, verbose_name="Автор курса")
    date_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Student(AbstractUser):
    courses = models.ManyToManyField(
        Course, blank=True, related_name="student_courses", verbose_name="Курсы пользователя")

    def __str__(self):
        return self.get_username()

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    name = models.CharField(max_length=150, db_index=True, verbose_name="Название урока")
    description = models.TextField(blank=True, verbose_name="Описание урока")
    content = models.TextField(verbose_name="Контент")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Order(models.Model):
    student = models.ForeignKey(Student, related_name="orders", on_delete=models.CASCADE, verbose_name="Пользователь")
    course = models.ManyToManyField(Course, related_name="order_courses", verbose_name="Курсы")
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Заказ курса"
        verbose_name_plural = "Заказы курсов"